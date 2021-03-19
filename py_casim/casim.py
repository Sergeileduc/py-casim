"""Code to upload an image and get his share url."""

import logging
from pathlib import Path

import requests

from .tools import (get_all_shares, get_all_shares_loggedin, get_folder_id,
                    get_image_id, get_share, get_share_loggedin)

logger = logging.getLogger(__name__)


class Casim():
    """Upload image to Casimages and get share url/code."""

    # CASIMAGES
    _url = "https://www.casimages.com/"
    _url_upload = "https://www.casimages.com/upload_ano_multi.php"
    _url_casi_share = "https://www.casimages.com/codes_ano_multi.php"
    _url_resize = "https://www.casimages.com/ajax/s_ano_resize.php"
    #: Valid resize values for resize keyword argument
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
        """Init Casim() object with image path, and optionnal resize value."""
        self.image = image
        self.resize = resize if str(resize) in self.resize_values else None
        self.image_id = None

        self.session = requests.Session()  # Session (keep cookies)
        self.session.get(Casim._url)  # Init for cookies

        self._set_resize()

        logger.info('casim created with image: "%s" and resize: %s',
                    self.image, self.resize)

    def __repr__(self):
        return f'Casim({self.image}, resize={self.resize})'

    def _set_resize(self):
        if self.resize:
            params = {"dim": self.resize}
            self.session.get(Casim._url_resize, params=params)
            logger.info('ask for resize with value %s', self.resize)

    def _upload_image(self):
        """Upload image and return id."""
        with open(self.image, 'rb') as f:
            file_ = {'Filedata': ('image', f, 'image/jpg')}
            r = self.session.post(Casim._url_upload,
                                  files=file_, headers=Casim._headers)

        self.image_id = r.text  # casimages share page ID
        logger.info('upload is ok, image id is %s', self.image_id)
        return self.image_id

    def _get_share(self, index=None):
        """Get share link/code.

        Args:
            index (int, optional): sqdfsdf. Defaults to None.
            0 :     Direct link (Mail & Messenger)
            1 :     Direct link (Forum, Blog, Site)
            2 :     HTML Code Thumbnail
            3 :     HTML Code Big
            4 :     Forum BBCode Thumbnail
            5 :     Forum BBCode Big
            6 :     Source Link Thumbnail
            7 :     Source Link Big

        Returns:
            str (or list): image share url (or list of share urls)
        """
        params = {"img": self.image_id}
        r = self.session.get(Casim._url_casi_share, params=params)
        logger.info('get() on share page returns code : %d', r.status_code)

        return get_share(r.text, index) if index else get_all_shares(r.text)

    def get_link(self):
        """Upload image and return share link (Big source link).

        Perform same thing as get_share_code(index=7).
        """
        self._upload_image()
        return self._get_share(7)

    def get_share_code(self, index=0):
        """Get share link/code.

        Args:
            index (int, optional): Url/code choice. Defaults to 0.
            0 :     Direct link (Mail & Messenger)
            1 :     Direct link (Forum, Blog, Site)
            2 :     HTML Code Thumbnail
            3 :     HTML Code Big
            4 :     Forum BBCode Thumbnail
            5 :     Forum BBCode Big
            6 :     Source Link Thumbnail
            7 :     Source Link Big

        Returns:
            str: image share url/code
        """
        self._upload_image()
        return self._get_share(index)

    def get_all(self):
        """Get list of all links/code.

            * Direct link (Mail & Messenger)
            * Direct link (Forum, Blog, Site)
            * HTML Code Thumbnail
            * HTML Code Big
            * Forum BBCode Thumbnail
            * Forum BBCode Big
            * Source Link Thumbnail
            * Source Link Big

        Returns:
            list -- all image share codes/links
        """
        self._upload_image()
        return self._get_share()


class CasimLogged():
    """Upload image to Casimages account and get share url/code."""

    # CASIMAGES
    _url = "https://www.casimages.com/"
    _url_login = "https://www.casimages.com/connexion"
    _url_resize = "https://www.casimages.com/ajax/m_photos_p_resize.php"
    _url_upload = "https://www.casimages.com/upload_mb_dz_img.php"
    _url_casi_share = "https://www.casimages.com/ajax/m_photos_codes_img.php"  # noqa: E501
    _url_m_photos = "https://www.casimages.com/m_photos"
    _url_search = "https://www.casimages.com/m_rechercher"
    #: Valid resize values for resize keyword argument
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
        """Init Casim() object with image path, and optionnal resize value."""
        self.image = Path(image)
        self.resize = resize if str(resize) in self.resize_values else None
        self.image_id = None
        self.loggedin = False

        self.session = requests.Session()  # Session (keep cookies)
        self.session.get(Casim._url)  # Init for cookies

        logger.info('casim created with image: "%s" and resize: %s',
                    self.image, self.resize)

    def __repr__(self):
        return f'Casim({self.image}, resize={self.resize})'

    def login(self, email, mdp):
        """Connect to Casimages with your own account."""
        self.session.get(CasimLogged._url_login)

        payload = {"email": email, "mdp": mdp}
        self.session.post(CasimLogged._url_login, data=payload)
        self.loggedin = True

    def change_folder(self, name):
        """Change destination folder. Folder named "name" should exist."""
        r = self.session.get(CasimLogged._url_m_photos)
        folder_id = get_folder_id(r.text, name)
        if folder_id:
            payload = {"alb": folder_id}
            r = self.session.get(CasimLogged._url_m_photos, params=payload)

    def _set_resize(self):
        if self.resize:
            params = {"dim": self.resize}
            self.session.get(self._url_resize, params=params)
            logger.info('ask for resize with value %s', self.resize)

    def _upload_image(self):
        """Upload image and return id."""
        self._set_resize()
        with open(self.image, 'rb') as f:
            file_ = {'Filedata': (self.image.name, f, 'image/jpg')}
            self.session.post(CasimLogged._url_upload,
                              files=file_, headers=CasimLogged._headers)
        logger.info('upload is ok')

    def _get_share(self, index=None):
        """Get share link/code.

        Args:
            index (int, optional): sqdfsdf. Defaults to None.
            0 :     Direct link (Mail & Messenger)
            1 :     Direct link (Forum, Blog, Site)
            2 :     HTML Code Thumbnail
            3 :     HTML Code Big
            4 :     Forum BBCode Thumbnail
            5 :     Forum BBCode Big
            6 :     Source Link Thumbnail
            7 :     Source Link Big

        Returns:
            str (or list): image share url (or list of share urls)
        """
        payload = {"wf": "images", "q": self.image.name}
        r = self.session.post(CasimLogged._url_search, params=payload)
        image_id = get_image_id(r.text, self.image.name)
        if image_id:
            params = {"codimg": image_id}
            r = self.session.get(CasimLogged._url_casi_share, params=params)
            return get_share_loggedin(r.text, index) if index else get_all_shares_loggedin(r.text)  # noqa: E501

    def get_link(self):
        """Upload image and return share link (Big source link).

        Perform same thing as get_share_code(index=7).
        """
        self._upload_image()
        return self._get_share(7)

    def get_share_code(self, index=0):
        """Get share link/code.

        Args:
            index (int, optional): Url/code choice. Defaults to 0.
            0 :     Direct link (Mail & Messenger)
            1 :     Direct link (Forum, Blog, Site)
            2 :     HTML Code Thumbnail
            3 :     HTML Code Big
            4 :     Forum BBCode Thumbnail
            5 :     Forum BBCode Big
            6 :     Source Link Thumbnail
            7 :     Source Link Big

        Returns:
            str: image share url/code
        """
        self._upload_image()
        return self._get_share(index)

    def get_all(self):
        """Get list of all links/code.

            * Direct link (Mail & Messenger)
            * Direct link (Forum, Blog, Site)
            * HTML Code Thumbnail
            * HTML Code Big
            * Forum BBCode Thumbnail
            * Forum BBCode Big
            * Source Link Thumbnail
            * Source Link Big

        Returns:
            list -- all image share codes/links
        """
        self._upload_image()
        return self._get_share()
