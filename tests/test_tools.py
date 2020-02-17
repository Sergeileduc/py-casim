#!/usr/bin/env python

"""Tests for `py_casim.tools."""

import pytest

from py_casim.tools import get_share, get_all_shares


@pytest.fixture
def response(datadir):
    """Read html sample from resp.html file."""
    contents = (datadir / 'resp.html').read_text()
    return contents


def test_get_share(response):
    """Simple test for get_share()."""
    url_share = get_share(response, 7)
    expected = ("https://nsa40.casimages.com/img/"
                "2020/02/17/200217113356178313.png")
    assert url_share == expected


def test_get_all_shares(response):
    """Simple test for get_all_shares()."""
    res = get_all_shares(response)
    assert len(res) == 8  # site gives 8 different image links
