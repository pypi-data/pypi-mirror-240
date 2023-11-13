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

import random
import sys
from collections import namedtuple

import fauxfactory
import pytest

from easy_as_pypi_termio.ascii_table import generate_table

TableKeysValues = namedtuple("TableKeysValues", ("keys", "values"))


def test_generate_table_basic(basic_table, capsys):
    rows, headers = basic_table
    output_obj = sys.stdout
    generate_table(rows, headers, output_obj)
    out, err = capsys.readouterr()
    assert out and not err


# ***


def test_generate_table_cols_align(basic_table, capsys):
    rows, headers = basic_table
    output_obj = sys.stdout
    cols_align = ["l", "r", "l"] + ["l"] * (len(headers) - 3)
    generate_table(rows, headers, output_obj, cols_align=cols_align)
    out, err = capsys.readouterr()
    assert out and not err


# ***


def test_generate_table_max_width_1(basic_table, capsys):
    rows, headers = basic_table
    output_obj = sys.stdout
    with pytest.raises(SystemExit):
        generate_table(rows, headers, output_obj, max_width=1)
    out, err = capsys.readouterr()
    assert not out and err


# ***


def test_generate_table_tabulate_okay(basic_table, capsys):
    rows, headers = basic_table
    output_obj = sys.stdout
    # Any string other than 'texttable' or falsey will take 'tabulate' branch,
    # because 'tabulate' supports a bunch of options.
    #  table_type = 'tabulate'  # default tabulate table type
    table_type = "fancy_grid"  # specific tabulate table type
    generate_table(rows, headers, output_obj, table_type=table_type)
    out, err = capsys.readouterr()
    assert out and not err


def test_generate_table_tabulate_fail_table_type(basic_table, capsys):
    rows, headers = basic_table
    output_obj = sys.stdout
    table_type = "foo"  # unrecognized tabulate table type
    with pytest.raises(ValueError):
        generate_table(rows, headers, output_obj, table_type=table_type)


# ***


def test_generate_table_named_tuple_fail_textable(basic_table, capsys):
    rows, headers = basic_table
    tkv = TableKeysValues(headers, rows)
    output_obj = sys.stdout
    with pytest.raises(AttributeError):
        # This fails because generate_table treats rows as list,
        # and calls rows.insert.
        generate_table(rows=tkv, headers="rows", output_obj=output_obj)


def test_generate_table_named_tuple_fail_tabulate(basic_table, capsys):
    rows, headers = basic_table
    tkv = TableKeysValues(headers, rows)
    with pytest.raises(ValueError):
        generate_table(
            rows=tkv,
            headers="rows",
            table_type="tabulate",
            output_obj=sys.stdout,
        )


# ***


@pytest.fixture
def basic_table():
    ncols = random.randint(3, 5)
    nrows = random.randint(3, 5)

    headers = []
    for ncol in range(ncols):
        header = fauxfactory.gen_string("alphanumeric")
        headers.append(header)

    rows = []
    for nrow in range(nrows):
        row = []
        for ncol in range(ncols):
            if ncol == 0:
                cell = fauxfactory.gen_iplum(words=10, paragraphs=1)
            elif ncol == 1:
                cell = fauxfactory.gen_integer()
            else:
                cell = fauxfactory.gen_string("utf8")
            row.append(cell)
        rows.append(row)

    return rows, headers
