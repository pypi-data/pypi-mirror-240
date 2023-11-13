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

"""Methods for common terminal echo operations."""

import shutil

from .paging import click_echo
from .style import attr, fg

__all__ = (
    "echo_block_header",
    "highlight_value",
    # PRIVATE:
    #  '__format_block_header',
    # EXTERNAL:
    #  Callers might want to import click_echo from this module, because it
    #  feels more natural here (but it's in paging module because pager-aware).
    "click_echo",
)


# ***


def echo_block_header(title, **kwargs):
    click_echo()
    click_echo(__format_block_header(title, **kwargs))


def __format_block_header(title, sep="━", full_width=False):
    """"""

    def _fact_block_header():
        header = []
        append_highlighted(header, title)
        append_highlighted(header, hr_rule())
        return "\n".join(header)

    def append_highlighted(header, text):
        highlight_col = "red_1"
        header.append(
            "{}{}{}".format(
                fg(highlight_col),
                text,
                attr("reset"),
            )
        )

    def hr_rule():
        if not full_width:
            horiz_rule = sep * len(title)
        else:
            # NOTE: When piping (i.e., no tty), width defaults to 80.
            term_width = shutil.get_terminal_size().columns
            horiz_rule = "─" * term_width
        return horiz_rule

    return _fact_block_header()


# ***


def highlight_value(msg):
    # FIXME: (lb): Replace hardcoding. Assign from styles.conf. #styling
    highlight_color = "medium_spring_green"
    return "{}{}{}".format(fg(highlight_color), msg, attr("reset"))
