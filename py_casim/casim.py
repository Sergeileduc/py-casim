"""Code to upload an image and get his share url."""

import logging
import requests

from .tools import get_share, get_all_shares


logger = logging.getLogger(__name__)


class Casim():
    """Upload image to Casimages and get share url/code.
    """

    # CASIMAGES
    _url = "https://www.casimages.com/"
    _url_upload = "https://www.casimages.com/upload_ano_multi.php"
    _url_casi_share = "https://www.casimages.com/codes_ano_multi.php?img={}"
    resize_values = ["100", "125", "320", "640", "800", "1024", "1280", "1600"]

    _headers = {
        "Accept": "application/json",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",  # noqa: E501
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "X-Requested-With": "XMLHttpRequest"
              }

    def __init__(self, image, resize=None):
        self.image = image
        self.resize = resize if str(resize) in self.resize_values else None
        self.image_id = None

        self.session = requests.Session()  # Session (keep cookies)
        self.session.get(Casim._url)  # Init for cookies

        self._set_resize()

        logger.info(f'casim created with image: '
                    f'"{self.image}" and resize: {self.resize}')

    def _set_resize(self):
        if self.resize:
            self.url_resize = (f"https://www.casimages.com/"
                               f"ajax/s_ano_resize.php?dim={self.resize}")
            self.session.get(self.url_resize)
            logger.info(f'ask for resize with value {self.resize}'
                        f'and url : {self.url_resize}')

    def _upload_image(self):
        """Upload image and return id."""
        with open(self.image, 'rb') as f:
            file_ = {'Filedata': ('image', f, 'image/jpg')}
            r = self.session.post(Casim._url_upload,
                                  files=file_, headers=Casim._headers)

        self.image_id = r.text  # casimages share page ID
        logger.info(f'upload is ok, image id is {self.image_id}')
        return self.image_id

    def _get_share(self, index=None):
        """\b
        Get share link/code.

        Keyword Arguments:
            index {int} -- index of wanted share link (default: {None})
            0 :     Direct link (Mail & Messenger)
            1 :     Direct link (Forum, Blog, Site)
            2 :     HTML Code Thumbnail
            3 :     HTML Code Big
            4 :     Forum BBCode Thumbnail
            5 :     Forum BBCode Big
            6 :     Source Link Thumbnail
            7 :     Source Link Big
            None :  All of the above (list)
        Returns:
            str (or list) -- image share url (or list of share urls)
        """
        r = self.session.get(Casim._url_casi_share.format(self.image_id))
        logger.info(f'get() on share page returns code : {r.status_code}')
        if index:
            return get_share(r.text, index)
        else:
            return get_all_shares(r.text)

    def get_link(self):
        """Upload image and return share link (Big source link).
        Perform same thing as get_share_code(index=7)"""
        self._upload_image()
        return self._get_share(7)

    def get_share_code(self, index=0):
        """Get share link/code.

        Keyword Arguments:
            index {int} -- index of wanted share link (default: {0})
            0 :     Direct link (Mail & Messenger)
            1 :     Direct link (Forum, Blog, Site)
            2 :     HTML Code Thumbnail
            3 :     HTML Code Big
            4 :     Forum BBCode Thumbnail
            5 :     Forum BBCode Big
            6 :     Source Link Thumbnail
            7 :     Source Link Big
        Returns:
            str -- image share url/code
        """
        self._upload_image()
        return self._get_share(index)

    def get_all(self):
        """Return list of all links/code.
            Direct link (Mail & Messenger)
            Direct link (Forum, Blog, Site)
            HTML Code Thumbnail
            HTML Code Big
            Forum BBCode Thumbnail
            Forum BBCode Big
            Source Link Thumbnail
            Source Link Big

        Returns:
            list -- all image share codes/links
        """
        self._upload_image()
        return self._get_share()