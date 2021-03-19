"""Pytest global fixtures and conf."""

from pathlib import Path

import pytest
from requests import Session

from py_casim.casim import Casim, CasimLogged


@pytest.fixture
def mini_bbcode():
    """BBCODE share code."""
    bbcode = ('[URL=https://www.casimages.com/i/200217113356178313.png.html]'  # noqa: E501
              '[IMG]https://nsa40.casimages.com/img/2020/02/17/mini_200217113356178313.png[/IMG][/url]')  # noqa: E501
    return bbcode


@pytest.fixture
def response():
    """Read html sample from resp.html file."""
    # with open("tests/test_tools/resp.html", "r") as f:
    #     content = f.read_text()
    path = Path("tests/test_tools/resp.html")
    content = path.read_text()
    return content


@pytest.fixture
def response2():
    """Read html sample from resp.html file. (for CasimLoggedin)"""
    path = Path("tests/test_tools/response_loggedin_search.html")
    content = path.read_text()
    return content


@pytest.fixture
def response3():
    """Read html sample from resp.html file. (for CasimLoggedin)"""
    path = Path("tests/test_tools/resp_share_loggedin.html")
    content = path.read_text()
    return content


@pytest.fixture
def response4():
    """Read html sample from resp.html file. (for CasimLoggedin)"""
    path = Path("tests/test_tools/resp_folders.html")
    content = path.read_text()
    return content


class MockResponse:
    """Fake requests resonse."""

    def __init__(self, text, status_code):
        """Fake requests response object."""
        self.text = text
        self.status_code = status_code


@pytest.fixture(autouse=True)
def mock_session(monkeypatch, response, response2, response3, response4):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""
    image_id = "200217113356178313.png"

    def mock_get(*args, **kwargs):
        url = args[1]
        if url == Casim._url:
            return MockResponse("", 200)
        elif Casim._url_resize in url:
            return MockResponse("", 200)
        elif Casim._url_casi_share in url:
            return MockResponse(response, 200)
        elif CasimLogged._url_casi_share in url:
            return MockResponse(response3, 200)
        elif CasimLogged._url_m_photos in url:
            return MockResponse(response4, 200)
        else:
            return MockResponse("", 404)

    def mock_post(*args, **kwargs):
        url = args[1]
        if url == Casim._url_upload:
            return MockResponse(image_id, 200)
        elif CasimLogged._url_upload in url:
            return MockResponse("", 200)
        elif CasimLogged._url_search in url:
            return MockResponse(response2, 200)

    monkeypatch.setattr(Session, "get", mock_get)
    monkeypatch.setattr(Session, "post", mock_post)
