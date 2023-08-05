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


"""Tests of the Loom parse and serialise routines."""


from io import BytesIO

import breezy
import breezy.osutils
from breezy.plugins.loom.branch import EMPTY_REVISION
import breezy.plugins.loom.loom_io as loom_io
import breezy.plugins.loom.loom_state as loom_state
import breezy.revision
from breezy.tests import TestCase


class TestLoomIO(TestCase):

    def test_writer_constructors(self):
        loom_io.LoomWriter()
        state = loom_state.LoomState()
        loom_io.LoomStateWriter(state)

    def assertWritesThreadsCorrectly(self, expected_stream, threads):
        """Write threads through a LoomWriter and check the output and sha1."""
        writer = loom_io.LoomWriter()
        stream = BytesIO()
        expected_sha1 = breezy.osutils.sha_strings([expected_stream])
        self.assertEqual(expected_sha1, writer.write_threads(threads, stream))
        self.assertEqual(expected_stream, stream.getvalue())

    def test_write_empty_threads(self):
        self.assertWritesThreadsCorrectly(b'Loom meta 1\n', [])

    def test_write_threads(self):
        self.assertWritesThreadsCorrectly(
            b'Loom meta 1\n'
            b'empty: baseline\n'
            b'asdasdasdxxxrr not the baseline\n',
            [('baseline', EMPTY_REVISION),
             ('not the baseline', b'asdasdasdxxxrr')],
            )

    def test_write_unicode_threads(self):
        self.assertWritesThreadsCorrectly(
            b'Loom meta 1\n'
            b'empty: base\xc3\x9eline\n'
            b'asd\xc3\xadasdasdxxxrr not the baseline\n',
            [(u'base\xdeline', EMPTY_REVISION),
             ('not the baseline', u'asd\xedasdasdxxxrr'.encode('utf-8'))],
            )

    def assertWritesStateCorrectly(self, expected_stream, state):
        """Write state to a stream and check it against expected_stream."""
        writer = loom_io.LoomStateWriter(state)
        stream = BytesIO()
        writer.write(stream)
        self.assertEqual(expected_stream, stream.getvalue())

    def test_write_empty_state(self):
        state = loom_state.LoomState()
        self.assertWritesStateCorrectly(
            loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n\n',
            state)

    def test_write_state_with_parent(self):
        state = loom_state.LoomState()
        state.set_parents([b'1'])
        self.assertWritesStateCorrectly(
            loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n'
            b'1\n',
            state)

    def test_write_state_with_parents(self):
        state = loom_state.LoomState()
        state.set_parents([b'1', u'2\xeb'.encode('utf-8')])
        self.assertWritesStateCorrectly(
            loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n'
            b'1 2\xc3\xab\n',
            state)

    def test_write_state_with_threads(self):
        state = loom_state.LoomState()
        state.set_threads(
            [('base ', b'baserev', []),
             (u'\xedtop', b'\xc3\xa9toprev', []),
             ])
        self.assertWritesStateCorrectly(
            loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n'
            b'\n'
            b' : baserev base \n'
            b' : \xc3\xa9toprev \xc3\xadtop\n',
            state)

    def test_write_state_with_threads_and_parents(self):
        state = loom_state.LoomState()
        state.set_threads(
            [('base ', b'baserev', [None, None]),
             (u'\xedtop', b'\xc3\xa9toprev', [None, None]),
             ])
        state.set_parents([b'1', u'2\xeb'.encode('utf-8')])
        self.assertWritesStateCorrectly(
            loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n'
            b'1 2\xc3\xab\n'
            b'   : baserev base \n'
            b'   : \xc3\xa9toprev \xc3\xadtop\n',
            state)

    def assertReadState(self, parents, threads, state_stream):
        """Check that the state in stream can be read correctly."""
        state_reader = loom_io.LoomStateReader(state_stream)
        self.assertEqual(parents, state_reader.read_parents())
        self.assertEqual(threads, state_reader.read_thread_details())

    def test_read_state_empty(self):
        state_stream = BytesIO(loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n\n')
        self.assertReadState([], [], state_stream)

    def test_read_state_no_parents_threads(self):
        state_stream = BytesIO(
            loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n'
            b'\n'
            b' : baserev base \n'
            b' : \xc3\xa9toprev \xc3\xadtop\n')  # yes this is utf8
        self.assertReadState(
            [],
            [('base ', b'baserev', []),
             # name -> unicode, revid -> utf8
             (u'\xedtop', b'\xc3\xa9toprev', []),
             ],
            state_stream)

    def test_read_state_parents(self):
        state_stream = BytesIO(
            loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n'
            b'1 2\xc3\xab\n')
        self.assertReadState(
            [b'1', b'2\xc3\xab'],
            [],
            state_stream)

    def test_read_state_parents_threads(self):
        state_stream = BytesIO(
            loom_io._CURRENT_LOOM_FORMAT_STRING + b'\n'
            b'1 2\xc3\xab\n'
            b'   : baserev base \n'
            b'   : \xc3\xa9toprev \xc3\xadtop\n')  # yes this is utf8
        self.assertReadState(
            [b'1', b'2\xc3\xab'],
            [('base ', b'baserev', [None, None]),
             (u'\xedtop', b'\xc3\xa9toprev', [None, None]),
             ],
            state_stream)
