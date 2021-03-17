"""Some Beautiful soup functions."""

from bs4 import BeautifulSoup


def get_soup(html):
    """Transofm html in BeautifulSoup."""
    return BeautifulSoup(html, 'html.parser')


def _get_inputs(html):
    soup = get_soup(html)
    col = soup.select_one("div.col-sm-9")
    return [i["value"] for i in col.select("input.form-control")]


def _get_inputs2(html):
    soup = get_soup(html)
    return [i["value"] for i in soup.select("div.col-lg-6 > input.form-control")]  # noqa: E501


def get_share(html, index):
    """Get the share with given index.

    Args:
        html (str): input html
        index (int): index of wanted result (0 to 7)

    Returns:
        str: url or code to share image
    """
    return _get_inputs(html)[index]


def get_share_loggedin(html, index):
    """Get the share with given index.

    Args:
        html (str): input html
        index (int): index of wanted result (0 to 7)

    Returns:
        str: url or code to share image
    """
    return _get_inputs2(html)[index]


def get_all_shares(html):
    """Get all url/codes to share image."""
    return _get_inputs(html)


def get_all_shares_loggedin(html):
    """Get all url/codes to share image."""
    return _get_inputs2(html)


def get_folder_id(html, name):
    """Search folder by its name, and return his ID."""
    soup = get_soup(html)
    # print(soup.prettify())
    albs = soup.find_all('option', id='reptogo')
    for a in albs:
        if a.next_element == name:
            return a.get('value')
    return None


def get_image_id(html, name):
    """Search image by its name and return ID."""
    soup = get_soup(html)
    res = soup.select_one("#draggable")
    if res:
        return res.get('name')
