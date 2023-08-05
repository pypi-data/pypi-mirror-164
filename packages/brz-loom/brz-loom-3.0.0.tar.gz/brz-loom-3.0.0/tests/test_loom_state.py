# Loom, a plugin for bzr to assist in developing focused patches.
# Copyright (C) 2006 - 2008 Canonical Limited.
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


"""Tests of the Loom current-state object."""


from io import BytesIO

import breezy.plugins.loom.loom_io as loom_io
import breezy.plugins.loom.loom_state as loom_state
from breezy.revision import NULL_REVISION
from breezy.tests import TestCase


class TestLoomState(TestCase):

    def test_default_constructor(self):
        state = loom_state.LoomState()
        # the default object must have no parents and no threads.
        self.assertEqual([], state.get_parents())
        self.assertEqual([], state.get_threads())
        self.assertEqual(NULL_REVISION, state.get_basis_revision_id())
        self.assertEqual({}, state.get_threads_dict())

    def test_reader_constructor(self):
        # make a state
        state = loom_state.LoomState()
        state.set_threads(
            [('name', b'rev', [None, None]),
             ('dangerous name', b'rev2', [None, None])])
        state.set_parents([b'bar', b'am'])
        stream = BytesIO()
        writer = loom_io.LoomStateWriter(state)
        writer.write(stream)
        # creating state from a serialised loom
        stream.seek(0)
        reader = loom_io.LoomStateReader(stream)
        state = loom_state.LoomState(reader)
        self.assertEqual([b'bar', b'am'], state.get_parents())
        self.assertEqual(
            [('name', b'rev', [None, None]),
             ('dangerous name', b'rev2', [None, None])],
            state.get_threads())
        self.assertEqual(b'bar', state.get_basis_revision_id())

    def test_set_get_threads(self):
        state = loom_state.LoomState()
        sample_threads = [('foo', b'bar', []), (u'g\xbe', b'bar', [])]
        state.set_threads(sample_threads)
        self.assertEqual([], state.get_parents())
        self.assertEqual(NULL_REVISION, state.get_basis_revision_id())
        self.assertEqual(sample_threads, state.get_threads())
        # alter the sample threads we just set, to see that the stored copy is
        # separate
        sample_threads.append('foo')
        self.assertNotEqual(sample_threads, state.get_threads())
        # and check the returned copy is also independent.
        sample_threads = state.get_threads()
        sample_threads.append('foo')
        self.assertNotEqual(sample_threads, state.get_threads())

    def test_set_get_parents(self):
        state = loom_state.LoomState()
        sample_threads = [('foo', b'bar', [])]
        state.set_threads(sample_threads)
        # can set parents to nothing with no side effects
        state.set_parents([])
        self.assertEqual([], state.get_parents())
        self.assertEqual(NULL_REVISION, state.get_basis_revision_id())
        self.assertEqual(sample_threads, state.get_threads())
        # can set a single parent with no threads
        state.set_parents([b'foo'])
        self.assertEqual([b'foo'], state.get_parents())
        self.assertEqual(b'foo', state.get_basis_revision_id())
        self.assertEqual(sample_threads, state.get_threads())
        # can set a single parent with threads
        state.set_parents([b'bar'])
        self.assertEqual([b'bar'], state.get_parents())
        self.assertEqual(b'bar', state.get_basis_revision_id())
        self.assertEqual(sample_threads, state.get_threads())
        # can set multiple parents
        state.set_parents([b'bar', b' am'])
        self.assertEqual([b'bar', b' am'], state.get_parents())
        self.assertEqual(b'bar', state.get_basis_revision_id())
        self.assertEqual(sample_threads, state.get_threads())

    def get_sample_state(self):
        state = loom_state.LoomState()
        sample_threads = [('foo', b'bar', []), (u'g\xbe', b'bar', [])]
        state.set_threads(sample_threads)
        return state

    def test_get_threads_dict(self):
        state = self.get_sample_state()
        self.assertEqual(
            {'foo': (b'bar', []),
             u'g\xbe': (b'bar', []),
             },
            state.get_threads_dict())

    def test_thread_index(self):
        state = self.get_sample_state()
        self.assertEqual(0, state.thread_index('foo'))
        self.assertEqual(1, state.thread_index(u'g\xbe'))

    def test_new_thread_after_deleting(self):
        state = self.get_sample_state()
        self.assertEqual(u'g\xbe', state.get_new_thread_after_deleting('foo'))
        self.assertEqual('foo', state.get_new_thread_after_deleting(u'g\xbe'))

    def test_new_thread_after_deleting_one_thread(self):
        state = loom_state.LoomState()
        state.set_threads([('foo', b'bar', [])])
        self.assertIs(None, state.get_new_thread_after_deleting('foo'))
