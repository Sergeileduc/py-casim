=====
Usage
=====

*******************
Import as a package
*******************

To use Python Casim in a project::

    from py_casim import Casim

    c = Casim("my_image.jpg")

    link = c.get_link()

    print(link)

To resize an image::

    from py_casim import Casim

    c = Casim("my_image.jpg", resize=640)

    link = c.get_link()

    print(link)


To get other urls/ code (like HTML or BBCode)::

    from py_casim import Casim

    c = Casim("my_image.jpg")

    res = c.get_share_code(index=3)

    print(res)


***********************
Use Command Line Script
***********************


In your terminal ::

    py_casim my_image.jpg


Or ::

    py_casim --size 640 my_image.jpg


For more ::

    py_casim --help

    Usage: py_casim [OPTIONS] FILENAME

    Upload an image to Casimages, and get url back.
    Resizing is optionnal (125x125, 320x240, 640x480, etc...)
    Default returned url is the Source Link (Big).
    Use the option to get different url format, or use --all option.

    Examples :
        py_casim my_image.jpg

        py_casim --all my_image.jpg

        py_casim -s 640 my_image.jpg

        py_casim --size 320 --code 3 my_image.jpg

    Options:
    -a, --all                       Get all urls and codes (HTML/BBcode) back.
    -s, --size [100|125|320|640|800|1024|1280|1600]
                                    Value for image resizing. Optional.
    -c, --code INTEGER RANGE        Choose desired url/code.
                                    0 Direct link (Mail
                                    & Messenger)
                                    1 Direct link (Forum, Blog,
                                    Site)
                                    2 HTML Code Thumbnail
                                    3 HTML Code Big
                                    4 Forum BBCode Thumbnail
                                    5 Forum BBCode Big
                                    6 Source Link Thumbnail
                                    7 Source Link Big
    --help                          Show this message and exit.


