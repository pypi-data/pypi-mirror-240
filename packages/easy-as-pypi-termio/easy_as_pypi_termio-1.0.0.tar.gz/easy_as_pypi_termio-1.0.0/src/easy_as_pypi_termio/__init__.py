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

"""Top-level package for this CLI-based application."""

# Convenience imports.
#
# - Usage: Lets you simplify imports, e.g., these as equivalent:
#
#     from easy_as_pypi_termio.echoes import click_echo
#
#     from easy_as_pypi_termio import click_echo
#
# - Note: Disable the imported-but-not-used linter rule:
#
#     noqa: F401: Disable: 'foo.bar' imported but unused.

from .echoes import echo_block_header, highlight_value  # noqa: F401
from .errors import (  # noqa: F401
    echo_exit,
    echo_warning,
    exit_warning,
    exit_warning_crude,
)
from .paging import ClickEchoPager, click_echo  # noqa: F401
from .style import attr, bg, coloring, fg, stylize  # noqa: F401

# This version is substituted on poetry-build by poetry-dynamic-versioning.
# - Consequently, __version__ remains empty when installed in 'editable' mode.
__version__ = "1.0.0"
