# Python Casim

[![PyPI](https://img.shields.io/pypi/v/py-casim.svg)](https://pypi.org/project/py-casim/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-casim)
[![Build Status](https://travis-ci.org/Sergeileduc/py-casim.svg?branch=master)](https://travis-ci.org/Sergeileduc/py-casim)
[![Documentation Status](https://readthedocs.org/projects/py-casim/badge/?version=latest)](https://py-casim.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/Sergeileduc/py-casim/branch/master/graph/badge.svg)](https://codecov.io/gh/Sergeileduc/py-casim)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dc2020cf808b4af2b40c592e8b0cec5d)](https://www.codacy.com/manual/sergei.leduc/py-casim?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sergeileduc/py-casim&amp;utm_campaign=Badge_Grade)
[![Requirements Status](https://requires.io/github/Sergeileduc/py-casim/requirements.svg?branch=master)](https://requires.io/github/Sergeileduc/py-casim/requirements/?branch=master)

Python package and cli to upload image on Casimages.

## In python project

```python
from py_casim import Casim

c = Casim("my_image.jpg")

link = c.get_link()

print(link)
```

To resize an image :

```python
from py_casim import Casim

c = Casim("my_image.jpg", resize=640)

link = c.get_link()

print(link)
```

To get another url/code return :

```python
from py_casim import Casim

c = Casim("my_image.jpg", resize=640)

link = c.get_share_code(3)  # return HTML code
```

See the doc for details.

## From command line

```console
foo@bar:~$ py-casim my_image.jpg
https://nsa40.casimages.com/img/xxxxxxxxxxxxxxx.png
```

or with options :

```console
foo@bar:~$ py-casim --size 640 my_image.jpg
https://nsa40.casimages.com/img/xxxxxxxxxxxxxxx.png
```

*   Free software: MIT license
*   Documentation: <https://py-casim.readthedocs.io>.

### Features

*   upload image and get his url
*   python package (import) OR command line tool

### Credits

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template.

`Cookiecutter`: <https://github.com/audreyr/cookiecutter>

`audreyr/cookiecutter-pypackage`: <https://github.com/audreyr/cookiecutter-pypackage>
