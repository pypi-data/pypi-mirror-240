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

from easy_as_pypi_termio.style import map_color  # Unimplemented
from easy_as_pypi_termio.style import (
    attr,
    bg,
    coloring,
    disable_colors,
    enable_colors,
    fg,
    set_coloring,
    stylize,
    verify_colors_attrs,
)


class TestStyle:
    # ***

    def test_style_enable_colors(self):
        assert not coloring()
        enable_colors()
        assert coloring()
        disable_colors()
        assert not coloring()

    def test_set_coloring(self):
        was_coloring = set_coloring(True)
        assert not was_coloring
        was_coloring = set_coloring(False)
        assert was_coloring

    # ***

    BLUE_NO = ""
    BLUE_FG = "\x1b[38;5;4m"
    BLUE_BG = "\x1b[48;5;4m"

    BOLD_NO = ""
    BOLD_ON = "\x1b[1m"

    def test_fg_coloring_off(self):
        text = fg(color="blue")
        assert text == self.BLUE_NO

    def test_fg_coloring_on(self, enable_coloring):
        text = fg(color="blue")
        assert text == self.BLUE_FG

    def test_bg_coloring_off(self):
        text = bg(color="blue")
        assert text == self.BLUE_NO

    def test_bg_coloring_on(self, enable_coloring):
        text = bg(color="blue")
        assert text == self.BLUE_BG

    def test_attr_coloring_off(self):
        text = attr(color="bold")
        assert text == self.BOLD_NO

    def test_attr_coloring_on(self, enable_coloring):
        text = attr(color="bold")
        assert text == self.BOLD_ON

    # ***

    def test_stylize_off(self):
        foo = object()
        assert stylize(foo) is foo

    def test_stylize_on(self, enable_coloring):
        text = stylize("This is loud ’n green", "bold", "green")
        assert text == "\x1b[1mThis is loud ’n green\x1b[0m"

    # ***

    def test_verify_colors_attrs(self):
        attrs = ["bold", "bolder", "blue", "bluer"]
        errs = verify_colors_attrs(*attrs)
        assert errs == ["bolder", "bluer"]

    # ***

    def test_map_color(self):
        # 2020-12-21: Apparently unimplemented. Must've forgot.
        foo = object()
        assert map_color(foo) is foo


# ***
