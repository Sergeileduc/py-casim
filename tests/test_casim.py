#!/usr/bin/env python

"""Tests for `py_casim` package."""

import re
import pytest

from py_casim.casim import Casim


@pytest.fixture(scope='function')
def casim_inst(datadir):
    """Instantiate a casim objetc with sample image.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    image = (datadir / 'sample image.png')
    return Casim(image, resize=125)


def test_repr(casim_inst):
    """Test __repr__."""
    print("coucou\n")
    print(repr(casim_inst))
    assert re.match(r"Casim(.*/test_casim/sample image.png, resize=125)",
                    repr(casim_inst))


def test_get_link(casim_inst):
    """Test Casim.get_link()."""
    res = casim_inst.get_link()
    expected = "https://nsa40.casimages.com/img/2020/02/17/200217113356178313.png"  # noqa: E501
    assert res == expected


def test_get_share(casim_inst):
    """Test Casim.get_share()."""
    res = casim_inst.get_share_code(4)
    expected = ('[URL=https://www.casimages.com/i/200217113356178313.png.html]'  # noqa: E501
                '[IMG]https://nsa40.casimages.com/img/2020/02/17/mini_200217113356178313.png[/IMG][/url]')  # noqa: E501
    assert res == expected
