#!/usr/bin/env python

"""Tests for `py_casim` package."""

import pytest
import re

from click.testing import CliRunner

from py_casim.casim import Casim
from py_casim import cli


@pytest.fixture(scope='function')
def casim_inst(datadir):
    """Instantiate a casim objetc with sample image.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    image = (datadir / 'sample image.jpg')
    return Casim(image, resize=125)


def test_share(casim_inst):
    """Test Casim.get_link()."""
    res = casim_inst.get_link()
    print(res)
    assert re.match(
        r'https://nsa40\.casimages\.com/img/\d{4}/\d{2}/\d{2}/\d+\.jpg', res)


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    # result = runner.invoke(cli.main)
    # assert result.exit_code == 0
    # assert 'py_casim.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help                          Show this message and exit.' in help_result.output  # noqa: E501
