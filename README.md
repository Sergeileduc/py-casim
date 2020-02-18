# Python Casim

[![PyPI](https://img.shields.io/pypi/v/py_casim.svg)](https://pypi.python.org/pypi/py_casim)
[![Build Status](https://travis-ci.org/Sergeileduc/py_casim.svg?branch=master)](https://travis-ci.org/Sergeileduc/py_casim)
[![Documentation Status](https://readthedocs.org/projects/py-casim/badge/?version=latest)](https://py-casim.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/Sergeileduc/py_casim/branch/master/graph/badge.svg)](https://codecov.io/gh/Sergeileduc/py_casim)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/de9d039dab414f2d82782bda6a8353fc)](https://app.codacy.com/manual/Sergeileduc/py_casim?utm_source=github.com&utm_medium=referral&utm_content=Sergeileduc/py_casim&utm_campaign=Badge_Grade_Dashboard)

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

```shell
py_casim my_image.jpg
```

or with options :

```shell
py_casim --size 640 my_image.jpg
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
