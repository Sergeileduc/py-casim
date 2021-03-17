#!/usr/bin/env python

"""Tests for `py_casim` package."""

import pytest
from click.testing import CliRunner

from py_casim import cli, __version__


@pytest.fixture(scope='module')
def runner():
    """Cli runner to be used in tests."""
    return CliRunner()


def test_cli_version(runner):
    """Test the CLI help command."""
    version_result = runner.invoke(cli.app, ['--version'])
    assert version_result.exit_code == 0
    assert version_result.output == 'py-casim version ' + __version__ + '\n'


def test_cli_help(runner):
    """Test the CLI help command."""
    help_result = runner.invoke(cli.app, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output


def test_cli_size_opt(runner):
    """Test the CLI with size opt."""
    resp = runner.invoke(cli.app, ['--size', '125', 'tests/data/sample image.png'])  # noqa: E501
    assert resp.exit_code == 0
    assert resp.output.rstrip() == 'https://nsa40.casimages.com/img/2020/02/17/200217113356178313.png'  # noqa: E501


def test_cli_all_opt(runner, mini_bbcode):
    """Test the CLI with --all opt."""
    resp = runner.invoke(cli.app, ['--all', 'tests/data/sample image.png'])  # noqa: E501
    assert resp.exit_code == 0
    lines = resp.output.splitlines()
    assert len(lines) == 8
    assert lines[4] == mini_bbcode


def test_cli_ode_opt(runner, mini_bbcode):
    """Test the CLI with --code opt."""
    resp = runner.invoke(cli.app, ['--code', 4, 'tests/data/sample image.png'])  # noqa: E501
    assert resp.exit_code == 0
    assert resp.output.rstrip() == mini_bbcode
