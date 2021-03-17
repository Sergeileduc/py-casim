#!/usr/bin/env python

"""Tests for `py_casim.tools."""

import pytest

from py_casim.tools import (get_all_shares, get_folder_id, get_image_id,
                            get_share, get_share_loggedin)


@pytest.fixture
def response(datadir):
    """Read html sample from resp.html file."""
    contents = (datadir / 'resp.html').read_text()
    return contents


@pytest.fixture
def response_folders(datadir):
    """Read html sample from resp.html file."""
    contents = (datadir / 'resp_folders.html').read_text()
    return contents


@pytest.fixture
def response_search_image(datadir):
    """Read html sample from resp.html file."""
    contents = (datadir / 'response_loggedin_search.html').read_text()
    return contents


@pytest.fixture
def response_share_loggedin(datadir):
    """Read html sample from resp.html file."""
    contents = (datadir / 'resp_share_loggedin.html').read_text()
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


def test_get_folder_id(response_folders):
    "Simple test for get_folder_id"
    res = get_folder_id(response_folders, "Scantrad")
    assert res == "428293"


def test_get_image_id(response_search_image):
    res = get_image_id(response_search_image, "sample image.png")
    assert res == '17320516'


def test_get_share_loggedin(response_share_loggedin):
    url = get_share_loggedin(response_share_loggedin, index=7)
    expected = "https://nsm09.casimages.com/img/2021/03/17//21031703204821371617320516.png"  # noqa: E501
    assert url == expected
