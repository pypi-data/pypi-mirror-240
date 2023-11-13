# This file exists within 'easy-as-pypi-termio':
#
#   https://github.com/tallybark/easy-as-pypi-termio#🍉
#
# Copyright © 2018-2020 Landon Bouma. All rights reserved.
#
# Permission is hereby granted,  free of charge,  to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge,  publish,  distribute, sublicense,
# and/or  sell copies  of the Software,  and to permit persons  to whom the
# Software  is  furnished  to do so,  subject  to  the following conditions:
#
# The  above  copyright  notice  and  this  permission  notice  shall  be
# included  in  all  copies  or  substantial  portions  of  the  Software.
#
# THE  SOFTWARE  IS  PROVIDED  "AS IS",  WITHOUT  WARRANTY  OF ANY KIND,
# EXPRESS OR IMPLIED,  INCLUDING  BUT NOT LIMITED  TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE  FOR ANY
# CLAIM,  DAMAGES OR OTHER LIABILITY,  WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE,  ARISING FROM,  OUT OF  OR IN  CONNECTION WITH THE
# SOFTWARE   OR   THE   USE   OR   OTHER   DEALINGS  IN   THE  SOFTWARE.

from unittest import mock

import click_hotoffthehamster as click
import pytest

from easy_as_pypi_termio.echoes import echo_block_header, highlight_value


@mock.patch.object(click, "echo")
def test_echo_block_header_basic(click_echo_mock):
    echo_block_header("foo")
    assert click_echo_mock.called


@pytest.mark.parametrize(("full_width",), ((True,), (False,)))
def test_echo_block_header_full_width(full_width, mocker):
    # @parametrize and @patch don't mix, apparently.
    click_echo_mock = mocker.patch.object(click, "echo")
    echo_block_header("foo", full_width=full_width)
    assert click_echo_mock.called


def test_highlight_value(enable_coloring):
    highlight_color = highlight_value("foo")
    assert highlight_color == "\x1b[38;5;49mfoo\x1b[0m"
