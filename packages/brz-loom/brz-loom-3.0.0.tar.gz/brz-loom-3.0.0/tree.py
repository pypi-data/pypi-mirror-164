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

"""The Loom Tree support routines.

LoomTreeDecorator decorates any tree which has a loomed branch to give it
loom-aware functionality.
"""

from __future__ import absolute_import

__all__ = ['LoomTreeDecorator']

from breezy import (
    trace,
    )
import breezy.errors
import breezy.merge
import breezy.revision

from breezy.plugins.loom.branch import EMPTY_REVISION


class LoomTreeDecorator(object):
    """Adapt any tree with a loomed branch to give it loom-aware methods.

    Currently this does not implemeny the Tree protocol itself. The decorated
    tree is available for use via the decorator.

    Useful attributes:
    tree: The decorated tree.
    branch: The branch of the decorated tree.
    """

    def __init__(self, a_tree):
        """Decorate a_tree with loom aware methods."""
        self.tree = a_tree
        self.branch = self.tree.branch

    def _check_switch(self):
        if self.tree.last_revision() != self.tree.branch.last_revision():
            raise breezy.errors.CommandError(
                'Cannot switch threads with an'
                ' out-of-date tree. Please run bzr update.')

    def up_thread(self, merge_type=None):
        """Move one thread up in the loom."""
        with self.lock_write():
            self._check_switch()
            # set it up:
            threadname = self.tree.branch.nick
            threads = self.tree.branch.get_loom_state().get_threads()
            old_thread_rev = None
            new_thread_name = None
            new_thread_rev = None
            # TODO: Factor this out into a search routine.
            for thread, rev, parents in reversed(threads):
                if thread == threadname:
                    # found the current thread.
                    old_thread_rev = rev
                    break
                new_thread_name = thread
                new_thread_rev = rev
            if new_thread_rev is None:
                raise breezy.errors.CommandError(
                    'Cannot move up from the highest thread.')
            graph = self.tree.branch.repository.get_graph()
            # special case no-change condition.
            if new_thread_rev == old_thread_rev:
                self.tree.branch._set_nick(new_thread_name)
                return 0
            if new_thread_rev == EMPTY_REVISION:
                new_thread_rev = breezy.revision.NULL_REVISION
            if old_thread_rev == EMPTY_REVISION:
                old_thread_rev = breezy.revision.NULL_REVISION
            # merge the tree up into the new patch:
            if merge_type is None:
                merge_type = breezy.merge.Merge3Merger
            try:
                merge_controller = breezy.merge.Merger.from_revision_ids(
                    self.tree, new_thread_rev, revision_graph=graph)
            except breezy.errors.UnrelatedBranches:
                raise breezy.errors.CommandError(
                    'corrupt loom: thread %s'
                    ' has no common ancestor with thread %s'
                    % (new_thread_name, threadname))
            merge_controller.merge_type = merge_type
            result = merge_controller.do_merge()
            # change the tree to the revision of the new thread.
            parent_trees = []
            if new_thread_rev != breezy.revision.NULL_REVISION:
                parent_trees.append(
                    (new_thread_rev, merge_controller.other_tree))
            # record the merge if:
            # the old thread != new thread (we have something to record)
            # and the new thread is not a descendant of old thread
            if (old_thread_rev != new_thread_rev
                    and not graph.is_ancestor(old_thread_rev, new_thread_rev)):
                basis_tree = self.tree.basis_tree()
                basis_tree.lock_read()
                parent_trees.append((old_thread_rev, basis_tree))
            else:
                basis_tree = None
            try:
                self.tree.set_parent_trees(parent_trees)
            finally:
                if basis_tree is not None:
                    basis_tree.unlock()
            if len(parent_trees) == 0:
                new_thread_rev = breezy.revision.NULL_REVISION
            else:
                new_thread_rev = parent_trees[0][0]
            # change the branch
            self.tree.branch.generate_revision_history(new_thread_rev)
            # update the branch nick.
            self.tree.branch._set_nick(new_thread_name)
            trace.note("Moved to thread '%s'." % new_thread_name)
            if (basis_tree is not None
                    and not result
                    and not self.tree.changes_from(basis_tree).has_changed()):
                trace.note("This thread is now empty, you may wish to "
                           'run "bzr combine-thread" to remove it.')
            if result != 0:
                return 1
            else:
                return 0

    def up_many(self, merge_type=None, target_thread=None):
        loom_state = self.branch.get_loom_state()
        threads = loom_state.get_threads()
        if target_thread is None:
            target_thread = threads[-1][0]
            if self.branch.nick == target_thread:
                raise breezy.errors.CommandError(
                    'Cannot move up from the highest thread.')
        else:
            upper_thread_i = loom_state.thread_index(target_thread)
            lower_thread_i = loom_state.thread_index(self.branch.nick)
            if lower_thread_i > upper_thread_i:
                raise breezy.errors.CommandError(
                    "Cannot up-thread to lower thread.")
        while self.branch.nick != target_thread:
            old_nick = self.branch.nick
            result = self.up_thread(merge_type)
            if result != 0:
                return result
            if len(self.tree.get_parent_ids()) > 1:
                self.tree.commit('Merge %s into %s' % (old_nick,
                                                       self.branch.nick))

    def down_thread(self, name=None):
        """Move to a thread down in the loom.

        :param name: If None, use the next lower thread; otherwise the nae of
            the thread to move to.
        """
        with self.lock_write():
            self._check_switch()
            threadname = self.tree.branch.nick
            state = self.tree.branch.get_loom_state()
            threads = state.get_threads()
            old_thread_index = state.thread_index(threadname)
            old_thread_rev = threads[old_thread_index][1]
            if name is None:
                if old_thread_index == 0:
                    raise breezy.errors.CommandError(
                        'Cannot move down from the lowest thread.')
                new_thread_name, new_thread_rev, _ = (
                    threads[old_thread_index - 1])
            else:
                new_thread_name = name
                index = state.thread_index(name)
                new_thread_rev = threads[index][1]
            assert new_thread_rev is not None
            self.tree.branch._set_nick(new_thread_name)
            if new_thread_rev == old_thread_rev:
                # fast path no-op changes
                breezy.trace.note("Moved to thread '%s'." % new_thread_name)
                return 0
            if new_thread_rev == EMPTY_REVISION:
                new_thread_rev = breezy.revision.NULL_REVISION
            if old_thread_rev == EMPTY_REVISION:
                old_thread_rev = breezy.revision.NULL_REVISION
            repository = self.tree.branch.repository
            try:
                basis_tree = self.tree.revision_tree(old_thread_rev)
            except breezy.errors.NoSuchRevisionInTree:
                basis_tree = repository.revision_tree(old_thread_rev)
            to_tree = repository.revision_tree(new_thread_rev)
            result = breezy.merge.merge_inner(
                self.tree.branch,
                to_tree,
                basis_tree,
                this_tree=self.tree)
            branch_revno, branch_revision = (
                self.tree.branch.last_revision_info())
            graph = repository.get_graph()
            new_thread_revno = graph.find_distance_to_null(
                new_thread_rev, [(branch_revision, branch_revno)])
            self.tree.branch.set_last_revision_info(new_thread_revno,
                                                    new_thread_rev)
            if new_thread_rev == breezy.revision.NULL_REVISION:
                parent_list = []
            else:
                parent_list = [(new_thread_rev, to_tree)]
            self.tree.set_parent_trees(parent_list)
            breezy.trace.note("Moved to thread '%s'." % new_thread_name)
            return result

    def lock_write(self):
        return self.tree.lock_write()

    def revert_loom(self, thread=None):
        """Revert the loom. This function takes care of tree state for revert.

        If the current loom is not altered, the tree is not altered. If it is
        then the tree will be altered as 'most' appropriate.

        :param thread: Only revert a single thread.
        """
        with self.lock_write():
            self._check_switch()
            current_thread = self.branch.nick
            last_rev = self.tree.last_revision()
            state = self.branch.get_loom_state()
            current_thread_rev = self.branch.last_revision()
            if thread is None:
                self.branch.revert_loom()
            else:
                self.branch.revert_thread(thread)
            state = self.branch.get_loom_state()
            threads_dict = state.get_threads_dict()
            # TODO find the next up thread if needed
            if not threads_dict:
                # last thread nuked
                to_rev = breezy.revision.NULL_REVISION
            elif current_thread != self.branch.nick:
                # thread change occured
                to_rev = threads_dict[self.branch.nick][0]
            else:
                # same thread tweaked
                if last_rev == threads_dict[current_thread][0]:
                    return
                to_rev = threads_dict[current_thread]
            if current_thread_rev == EMPTY_REVISION:
                current_thread_rev = breezy.revision.NULL_REVISION
            if to_rev == EMPTY_REVISION:
                to_rev = breezy.revision.NULL_REVISION
            # the thread changed, do a merge to match.
            basis_tree = self.tree.branch.repository.revision_tree(
                current_thread_rev)
            to_tree = self.tree.branch.repository.revision_tree(to_rev)
            breezy.merge.merge_inner(
                self.tree.branch,
                to_tree,
                basis_tree,
                this_tree=self.tree)
            self.tree.set_last_revision(to_rev)

    def unlock(self):
        self.tree.unlock()
