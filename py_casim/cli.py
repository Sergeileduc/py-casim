"""Console script for py_casim."""
import sys
import click
from .casim import Casim


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-a', '--all', is_flag=True,
              help='Get all urls and codes (HTML/BBcode) back.')
@click.option('-s', '--size', type=click.Choice(Casim.resize_values),
              default=None,
              help='Value for image resizing. Optional.')
@click.option('-c', '--code', type=click.IntRange(0, 7),
              default=None,
              help='''Choose desired url/code.
              0 Direct link (Mail & Messenger)
              1 Direct link (Forum, Blog, Site)
              2 HTML Code Thumbnail
              3 HTML Code Big
              4 Forum BBCode Thumbnail
              5 Forum BBCode Big
              6 Source Link Thumbnail
              7 Source Link Big''')
def app(filename, size, code, all):  # pylint: disable=redefined-builtin  # noqa: D301,E501
    """
    Upload an image to Casimages, and get url back.

    \b
    Resizing is optionnal (125x125, 320x240, 640x480, etc...)
    Default returned url is the Source Link (Big).
    Use the option to get different url format, or use --all option.

    \b
    Examples :
        py_casim my_image.jpg

        py_casim --all my_image.jpg

        py_casim -s 640 my_image.jpg

        py_casim --size 320 --code 3 my_image.jpg
    """
    # click.echo(f"Will upload {click.format_filename(filename)} to Casimages")
    # if size:
    #     click.echo(f"Resizing with value : {size}")
    # else:
    #     click.echo("No resize")
    c = Casim(filename, resize=size)
    if all:
        res = c.get_all()
        for r in res:
            click.echo(r)
    else:
        if code:
            res = c.get_share_code(code)
            click.echo(res)
        else:
            url = c.get_link()
            click.echo(url)
    return 0


if __name__ == "__main__":
    sys.exit(app())  # pragma: no cover  # pylint: disable=no-value-for-parameter  # noqa: E501
