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

from easy_as_pypi_termio.paging import ClickEchoPager, click_echo, flush_pager


class TestClickEchoPager:
    def test_enable_paging(self):
        assert not ClickEchoPager.paging()
        ClickEchoPager.enable_paging()
        assert ClickEchoPager.paging()
        ClickEchoPager.disable_paging()
        assert not ClickEchoPager.paging()

    def test_set_paging(self):
        was_paging = ClickEchoPager.set_paging(True)
        assert not was_paging
        was_paging = ClickEchoPager.set_paging(False)
        assert was_paging

    @mock.patch.object(click, "echo")
    def test_write_paging_off(self, click_echo_mock, enable_coloring):
        ClickEchoPager.write("foo")
        assert click_echo_mock.called

    @mock.patch.object(click, "echo_via_pager")
    def test_write_paging_on_then_flush_pager(
        self,
        click_echo_via_pager_mock,
        enable_paging,
    ):
        ClickEchoPager.write("foo")
        assert not click_echo_via_pager_mock.called
        ClickEchoPager.flush_pager()
        assert click_echo_via_pager_mock.called

    # ***


# ***


@mock.patch.object(click, "echo")
def test_click_echo_and_flush_pager_decorator(click_echo_mock):
    @flush_pager
    def inner_test():
        click_echo("foo")

    inner_test()
    assert click_echo_mock.called


# ***


@pytest.fixture
def enable_paging():
    ClickEchoPager.set_paging(True)
    yield
    ClickEchoPager.set_paging(False)
