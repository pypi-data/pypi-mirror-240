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

from easy_as_pypi_termio.crude_progress import CrudeProgress


class TestCrudeProgress:
    @mock.patch.object(click, "echo")
    def test_enabled_off(self, click_echo_mock):
        progger = CrudeProgress(enabled=False)
        progger.click_echo_current_task(task="testing-disabled")
        progger.start_crude_progressor(task_descrip="testing-start")
        progger.step_crude_progressor("it", "just", "doesn't", "matter")
        assert not click_echo_mock.called

    @mock.patch.object(click, "echo")
    def test_enabled_on(self, click_echo_mock):
        progger = CrudeProgress(enabled=True)

        progger.click_echo_current_task(task="testing-echo")
        assert click_echo_mock.called
        click_echo_mock.reset_mock

        term_width, dot_count, fact_sep = progger.start_crude_progressor(
            task_descrip="testing-start",
        )
        assert click_echo_mock.called
        click_echo_mock.reset_mock

        # Set dot_count >= term_width to cover the if-branch in the function
        # (that has no else-branch). (And luckily this isn't JS coverage, or
        # we'd have to  hit the else branch, too, which doesn't exist.)
        term_width, dot_count, fact_sep = progger.step_crude_progressor(
            "testing-step",
            term_width,
            dot_count=term_width,
            fact_sep=fact_sep,
        )
        assert click_echo_mock.called
