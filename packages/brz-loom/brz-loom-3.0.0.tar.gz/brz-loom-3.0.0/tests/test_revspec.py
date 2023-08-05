# Loom, a plugin for bzr to assist in developing focused patches.
# Copyright (C) 2006 Canonical Limited.
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


"""Tests of the loom revision-specifiers."""


import breezy.errors
from breezy.plugins.loom.branch import NoLowerThread, NoSuchThread
from breezy.plugins.loom.tests import TestCaseWithLoom
import breezy.plugins.loom.tree
from breezy.revisionspec import RevisionSpec


class TestRevSpec(TestCaseWithLoom):

    def get_two_thread_loom(self):
        tree = self.get_tree_with_loom('source')
        tree.branch.new_thread('bottom')
        tree.branch.new_thread('top')
        tree.branch._set_nick('bottom')
        rev_id_bottom = tree.commit('change bottom')
        loom_tree = breezy.plugins.loom.tree.LoomTreeDecorator(tree)
        loom_tree.up_thread()
        rev_id_top = tree.commit('change top')
        return tree, loom_tree, rev_id_bottom, rev_id_top


class TestThreadRevSpec(TestRevSpec):
    """Tests of the ThreadRevisionSpecifier."""

    def test_thread_colon_at_bottom_errors(self):
        tree, loom_tree, rev_id, _ = self.get_two_thread_loom()
        loom_tree.down_thread()
        spec = RevisionSpec.from_string('thread:')
        self.assertRaises(NoLowerThread, spec.in_branch, tree.branch)

    def test_thread_colon_gets_next_lower_thread(self):
        tree, loom_tree, rev_id, _ = self.get_two_thread_loom()
        spec = RevisionSpec.from_string('thread:')
        self.assertEqual(rev_id, spec.in_branch(tree.branch)[1])

    def test_thread_colon_bad_name_errors(self):
        tree, loom_tree, _, _ = self.get_two_thread_loom()
        loom_tree.down_thread()
        spec = RevisionSpec.from_string('thread:foo')
        err = self.assertRaises(NoSuchThread, spec.in_branch, tree.branch)
        self.assertEqual('foo', err.thread)

    def test_thread_colon_name_gets_named_thread(self):
        tree, loom_tree, _, rev_id = self.get_two_thread_loom()
        loom_tree.down_thread()
        spec = RevisionSpec.from_string('thread:top')
        self.assertEqual(rev_id, spec.in_branch(tree.branch)[1])

    def test_thread_colon_name_gets_named_thread_revision_id(self):
        tree, loom_tree, _, rev_id = self.get_two_thread_loom()
        loom_tree.down_thread()
        spec = RevisionSpec.from_string('thread:top')
        self.assertEqual(rev_id, spec.as_revision_id(tree.branch))

    def test_thread_on_non_loom_gives_BzrError(self):
        tree = self.make_branch_and_tree('.')
        spec = RevisionSpec.from_string('thread:')
        err = self.assertRaises(
            breezy.errors.BzrError, spec.as_revision_id, tree.branch)
        self.assertFalse(err.internal_error)


class TestBelowRevSpec(TestRevSpec):
    """Tests of the below: revision specifier."""

    def test_below_gets_tip_of_thread_below(self):
        tree, loom_tree, _, rev_id = self.get_two_thread_loom()
        loom_tree.down_thread()
        expected_id = tree.branch.last_revision()
        loom_tree.up_thread()
        spec = RevisionSpec.from_string('below:')
        self.assertEqual(expected_id, spec.as_revision_id(tree.branch))

    def test_below_on_bottom_thread_gives_BzrError(self):
        tree, loom_tree, _, rev_id = self.get_two_thread_loom()
        loom_tree.down_thread()
        spec = RevisionSpec.from_string('below:')
        err = self.assertRaises(
            breezy.errors.BzrError, spec.as_revision_id, tree.branch)
        self.assertFalse(err.internal_error)

    def test_below_named_thread(self):
        tree, loom_tree, _, rev_id = self.get_two_thread_loom()
        loom_tree.down_thread()
        expected_id = tree.branch.last_revision()
        spec = RevisionSpec.from_string('below:top')
        self.assertEqual(expected_id, spec.as_revision_id(tree.branch))

    def test_below_on_non_loom_gives_BzrError(self):
        tree = self.make_branch_and_tree('.')
        spec = RevisionSpec.from_string('below:')
        err = self.assertRaises(
            breezy.errors.BzrError, spec.as_revision_id, tree.branch)
        self.assertFalse(err.internal_error)
