from bs4 import BeautifulSoup


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


def _get_inputs(html):
    soup = get_soup(html)
    col = soup.select_one("div.col-sm-9")
    return [i["value"] for i in col.select("input.form-control")]


def get_share(html, index):
    return _get_inputs(html)[index]


def get_all_shares(html):
    return _get_inputs(html)
