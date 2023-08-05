# Loom, a plugin for bzr to assist in developing focused patches.
# Copyright (C) 2006, 2008 Canonical Limited.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
#

"""Loom commands."""

from breezy import controldir, directory_service, workingtree
import breezy.commands
import breezy.branch
from breezy import errors
from breezy.option import Option
import breezy.trace
import breezy.transport


class cmd_loomify(breezy.commands.Command):
    """Add a loom to this branch.

    This creates a loom in your branch, which will alter the behaviour of
    bzr for a number of commands to manage a group of patches being evolved
    in parallel.

    You must have a branch nickname explicitly set to use this command, as the
    branch nickname becomes the 'base thread' of the loom.  You can specify
    the branch nick with the --base option.
    """

    takes_args = ['location?']
    takes_options = [Option('base', type=str,
                            help='The name to use for the base thread.')]

    def run(self, location='.', base=None):
        from breezy.plugins.loom.branch import loomify
        (target, path) = breezy.branch.Branch.open_containing(location)
        with target.lock_write():
            if base is not None:
                target.nick = base
            elif not target.get_config().has_explicit_nickname():
                raise errors.CommandError(
                    'You must specify --base or have a branch nickname set to'
                    ' loomify a branch')
            loomify(target)
            loom = target.controldir.open_branch()
        # requires a new lock as its a new instance, XXX: teach bzrdir about
        # format changes ?
        loom.new_thread(loom.nick)


class cmd_combine_thread(breezy.commands.Command):
    __doc__ = """Combine the current thread with the thread below it.

    This will currently refuse to operate on the last thread, but in the future
    will just turn the loom into a normal branch again.

    Use combine-thread to remove a thread which has been merged into upstream.

    In precise terms this will:
     * Remove the entry from the loom for the current thread.
     * Change threads to the thread below.
    """

    takes_options = [
        Option('force', help='Combine even if work in the thread is not '
               'integrated up or down the loom.'),
        ]

    def run(self, force=False):
        from breezy.plugins.loom.branch import (
            require_loom_branch,
            CannotCombineOnLastThread,
            )
        from breezy.plugins.loom.tree import LoomTreeDecorator
        (tree, path) = workingtree.WorkingTree.open_containing('.')
        require_loom_branch(tree.branch)
        with tree.lock_write():
            current_thread = tree.branch.nick
            state = tree.branch.get_loom_state()
            if not force:
                # Check for unmerged work.
                # XXX: Layering issue whom should be caring for the check, not
                # the command thats for sure.
                threads = state.get_threads()
                current_index = state.thread_index(current_thread)
                rev_below = None
                rev_current = threads[current_index][1]
                rev_above = None
                if current_index:
                    # There is a thread below
                    rev_below = threads[current_index - 1][1]
                if current_index < len(threads) - 1:
                    rev_above = threads[current_index + 1][1]
                graph = tree.branch.repository.get_graph()
                candidates = [
                    rev for rev in (rev_below, rev_current, rev_above) if rev]
                heads = graph.heads(candidates)
                # If current is not a head, its trivially merged, or
                # if current is == rev_below, its also merged, or
                # if there is only one thread its merged (well its not
                # unmerged).
                if (rev_current == rev_below or rev_current not in heads
                        or (rev_below is None and rev_above is None)):
                    merged = True
                else:
                    merged = False
                if not merged:
                    raise errors.CommandError(
                        "Thread '%s' has unmerged work"
                        ". Use --force to combine anyway." % current_thread)
            new_thread = state.get_new_thread_after_deleting(current_thread)
            if new_thread is None:
                raise CannotCombineOnLastThread()
            breezy.trace.note(
                "Combining thread '%s' into '%s'",
                current_thread, new_thread)
            LoomTreeDecorator(tree).down_thread(new_thread)
            tree.branch.remove_thread(current_thread)


class cmd_create_thread(breezy.commands.Command):
    """Add a thread to this loom.

    This creates a new thread in this loom and moves the branch onto that
    thread.

    The thread-name must be a valid branch 'nickname', and must not be the name
    of an existing thread in your loom.

    The new thread is created immediately after the current thread.
    """

    takes_args = ['thread']

    def run(self, thread):
        from breezy.plugins.loom.branch import create_thread
        (loom, path) = breezy.branch.Branch.open_containing('.')
        create_thread(loom, thread)


class cmd_show_loom(breezy.commands.Command):
    """Show the threads in this loom.

    Output the threads in this loom with the newest thread at the top and
    the base thread at the bottom. A => marker indicates the thread that
    'commit' will commit to.
    """

    takes_args = ['location?']

    def run(self, location='.'):
        from breezy.plugins.loom.branch import require_loom_branch
        (loom, path) = breezy.branch.Branch.open_containing(location)
        require_loom_branch(loom)
        with loom.lock_read():
            threads = loom.get_loom_state().get_threads()
            nick = loom.nick
            for thread, revid, parents in reversed(threads):
                if thread == nick:
                    symbol = '=>'
                else:
                    symbol = '  '
                self.outf.write(symbol + thread + '\n')


class cmd_switch(breezy.builtins.cmd_switch):
    """Set the branch of a checkout and update.

    For looms, this is equivalent to 'down-thread' when to_location is the name
    of a thread in the loom.
    For lightweight checkouts, this changes the branch being referenced.
    For heavyweight checkouts, this checks that there are no local commits
    versus the current bound branch, then it makes the local branch a mirror
    of the new location and binds to it.

    In both cases, the working tree is updated and uncommitted changes
    are merged. The user can commit or revert these as they desire.

    Pending merges need to be committed or reverted before using switch.
    """

    _original_command = None

    def _get_thread_name(self, loom, to_location):
        """Return the name of the thread pointed to by 'to_location'.

        Most of the time this will be the name of the thread, but if
        'to_location' is 'bottom:' it will be the name of the bottom thread.
        If 'to_location' is 'top:', then it'll be the name of the top thread.
        """
        aliases = {'bottom:': 0, 'top:': -1}
        if to_location in aliases:
            threads = loom.get_loom_state().get_threads()
            thread = threads[aliases[to_location]]
            return thread[0]
        return to_location

    def run(self, to_location=None, force=False, create_branch=False,
            revision=None, directory=None):
        from breezy.plugins.loom.branch import (
            create_thread,
            NoSuchThread,
            NotALoom,
            )
        from breezy.plugins.loom.tree import LoomTreeDecorator
        # The top of this is cribbed from bzr; because bzr isn't factored out
        # enough.
        if directory is None:
            directory = u'.'
        control_dir, path = controldir.ControlDir.open_containing(directory)
        if to_location is None:
            if revision is None:
                raise errors.CommandError(
                    'You must supply either a revision or a location')
            to_location = '.'
        try:
            from_branch = control_dir.open_branch()
        except errors.NotBranchError:
            from_branch = None
        if create_branch:
            if from_branch is None:
                raise errors.CommandError(
                    'cannot create branch without source branch')
            to_location = directory_service.directories.dereference(
                to_location)
        if from_branch is not None:
            # Note: reopens.
            (tree, path) = workingtree.WorkingTree.open_containing(directory)
            tree = LoomTreeDecorator(tree)
            try:
                if create_branch:
                    return create_thread(tree.branch, to_location)
                thread_name = self._get_thread_name(tree.branch, to_location)
                return tree.down_thread(thread_name)
            except (AttributeError, NoSuchThread, NotALoom):
                # When there is no thread its probably an external branch
                # that we have been given.
                raise errors.MustUseDecorated
        else:
            # switching to a relocated branch
            raise errors.MustUseDecorated

    def run_argv_aliases(self, argv, alias_argv=None):
        """Parse command line and run.

        If the command requests it, run the decorated version.
        """
        try:
            super(cmd_switch, self).run_argv_aliases(list(argv), alias_argv)
        except (errors.MustUseDecorated, errors.BzrOptionError):
            if self._original_command is None:
                raise
            self._original_command().run_argv_aliases(argv, alias_argv)


class cmd_record(breezy.commands.Command):
    """Record the current last-revision of this tree into the current thread.
    """

    takes_args = ['message']

    def run(self, message):
        from breezy.plugins.loom.branch import require_loom_branch
        (abranch, path) = breezy.branch.Branch.open_containing('.')
        require_loom_branch(abranch)
        abranch.record_loom(message)
        breezy.trace.note("Loom recorded.")


class cmd_revert_loom(breezy.commands.Command):
    """Revert part or all of a loom.

    This will update the current loom to be the same as the basis when --all
    is supplied. If no parameters or options are supplied then nothing will
    happen. If a thread is named, then only that thread is reverted to its
    state in the last committed loom.
    """

    takes_args = ['thread?']
    takes_options = [Option('all', help='Revert all threads.'),
                     ]

    def run(self, thread=None, all=None):
        if thread is None and all is None:
            breezy.trace.note('Please see revert-loom -h.')
            return
        from breezy.plugins.loom.branch import require_loom_branch
        from breezy.plugins.loom.tree import LoomTreeDecorator
        (tree, path) = workingtree.WorkingTree.open_containing('.')
        require_loom_branch(tree.branch)
        tree = LoomTreeDecorator(tree)
        if all:
            tree.revert_loom()
            breezy.trace.note('All threads reverted.')
        else:
            tree.revert_loom(thread)
            breezy.trace.note("thread '%s' reverted.", thread)


class cmd_down_thread(breezy.commands.Command):
    """Move the branch down a thread in the loom.

    This removes the changes introduced by the current thread from the branch
    and sets the branch to be the next thread down.

    Down-thread refuses to operate if there are uncommitted changes, since
    this is typically a mistake.  Switch can be used for this purpose, instead.
    """

    takes_args = ['thread?']
    aliases = ['down']
    _see_also = ['switch', 'up-thread']

    def run(self, thread=None):
        from breezy.plugins.loom.branch import require_loom_branch
        from breezy.plugins.loom.tree import LoomTreeDecorator
        (wt, path) = workingtree.WorkingTree.open_containing('.')
        require_loom_branch(wt.branch)
        tree = LoomTreeDecorator(wt)
        with tree.lock_write():
            basis = wt.basis_tree()
            with basis.lock_read():
                for change in wt.iter_changes(basis):
                    raise errors.CommandError(
                        'Working tree has uncommitted changes.')
            return tree.down_thread(thread)


class cmd_up_thread(breezy.commands.Command):
    """Move the branch up to the top thread in the loom.

    This merges the changes done in this thread but not incorporated into
    the next thread up into the next thread up and switches your tree to be
    that thread.  Unless there are conflicts, or --manual is specified, it
    will then commit and repeat the process.
    """

    takes_args = ['thread?']

    takes_options = ['merge-type', Option(
                'auto',
                help='Deprecated - now the default.'),
            Option('manual', help='Perform commit manually.'),
        ]

    _see_also = ['down-thread', 'switch']

    def run(self, merge_type=None, manual=False, thread=None, auto=None):
        from breezy.plugins.loom.branch import require_loom_branch
        from breezy.plugins.loom.tree import LoomTreeDecorator
        (tree, path) = workingtree.WorkingTree.open_containing('.')
        require_loom_branch(tree.branch)
        tree = LoomTreeDecorator(tree)
        if manual:
            if thread is not None:
                raise errors.CommandError('Specifying a thread does not'
                                             ' work with --manual.')
            return tree.up_thread(merge_type)
        else:
            return tree.up_many(merge_type, thread)


class cmd_export_loom(breezy.commands.Command):
    """Export loom threads as a full-fledged branches.

    LOCATION specifies the location to export the threads under.  If it does
    not exist, it will be created.

    In any of the standard config files, "export_loom_root" may be set to
    provide a default location that will be used if no location is supplied.
    """

    takes_args = ['location?']
    _see_also = ['configuration']

    def run(self, location=None):
        root_transport = None
        loom = breezy.branch.Branch.open_containing('.')[0]
        if location is None:
            location = loom.get_config().get_user_option('export_loom_root')
        if location is None:
            raise errors.CommandError('No export root known or specified.')
        root_transport = breezy.transport.get_transport(
            location, possible_transports=[loom.controldir.root_transport])
        root_transport.ensure_base()
        loom.export_threads(root_transport)
