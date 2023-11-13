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

from easy_as_pypi_termio.errors import (
    echo_exit,
    echo_warning,
    echoed_warnings_reset,
    exit_warning,
    exit_warning_crude,
)


@mock.patch.object(click, "echo")
def test_exit_warning_crude(click_echo_mock):
    with pytest.raises(SystemExit):
        exit_warning_crude("foo")
    assert click_echo_mock.called


@mock.patch.object(click, "echo")
def test_exit_warning(click_echo_mock):
    with pytest.raises(SystemExit):
        exit_warning("foo")
    assert click_echo_mock.called


@mock.patch.object(click, "echo")
def test_echo_warning(click_echo_mock):
    echo_warning("foo")
    assert click_echo_mock.called


@mock.patch.object(click, "echo")
def test_echoed_warnings_reset(click_echo_mock):
    echo_warning("foo")
    been_warned = echoed_warnings_reset()
    assert been_warned
    been_warned = echoed_warnings_reset()
    assert not been_warned


@mock.patch.object(click, "echo")
def test_echo_exit(click_echo_mock, mocker):
    ctx = mocker.MagicMock()
    echo_exit(ctx, "foo")
    assert click_echo_mock.called
    assert ctx.exit.called
