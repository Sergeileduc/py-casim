"""Nox sessions."""
import nox


@nox.session(reuse_venv=True)
def lint(session):
    """Lint code using flake8 and pydocstyle."""
    session.install("flake8", "pydocstyle")
    session.run("flake8", "py_casim", "tests")
    session.run("pydocstyle")


@nox.session(reuse_venv=True)
def tests(session):
    """Test with pytests."""
    # same as pip install -r -requirements-dev.txt
    session.install("-r", "requirements-dev.txt")
    session.run("pytest")
