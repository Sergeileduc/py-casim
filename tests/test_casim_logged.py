#!/usr/bin/env python

"""Tests for `py_casim` package."""

import re

import pytest

from py_casim.casim import CasimLogged


@pytest.fixture(scope='function')
def casim_inst(shared_datadir):
    """Instantiate a casim objetc with sample image.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    image = (shared_datadir / 'sample image.png')
    return CasimLogged(image, resize=125)


def test_repr(casim_inst):
    """Test __repr__."""
    assert re.match(r"Casim\((.*(/|\\)data(/|\\)sample image\.png), resize=125\)",  # noqa: E501
                    repr(casim_inst))


def test_get_link(casim_inst):
    """Test CasimLogged.get_link()."""
    casim_inst.change_folder("Scantrad")
    res = casim_inst.get_link()
    expected = "https://nsm09.casimages.com/img/2021/03/17//21031703204821371617320516.png"  # noqa: E501
    assert res == expected


def test_get_share(casim_inst):
    """Test CasimLogged.get_share()."""
    casim_inst.change_folder("Scantrad")
    res = casim_inst.get_share_code(4)
    expected = ('[URL=https://www.casimages.com/i/21031703204821371617320516.png.html]'  # noqa: E501
                '[IMG]https://nsm09.casimages.com/img/2021/03/17//mini_21031703204821371617320516.png[/IMG][/url]')  # noqa: E501
    assert res == expected


def test_get_all(casim_inst):
    """Test CasimLogged.get_all()."""
    casim_inst.change_folder("Scantrad")
    res = casim_inst.get_all()
    assert len(res) == 8
