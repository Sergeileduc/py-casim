"""Some Beautiful soup functions."""

from bs4 import BeautifulSoup


def get_soup(html):
    """Transofm html in BeautifulSoup."""
    return BeautifulSoup(html, 'html.parser')


def _get_inputs(html):
    soup = get_soup(html)
    col = soup.select_one("div.col-sm-9")
    return [i["value"] for i in col.select("input.form-control")]


def get_share(html, index):
    """Get the share with given index.

    Args:
        html (str): input html
        index (int): index of wanted result (0 to 7)

    Returns:
        str: url or code to share image
    """
    return _get_inputs(html)[index]


def get_all_shares(html):
    """Get all url/codes to share image."""
    return _get_inputs(html)
