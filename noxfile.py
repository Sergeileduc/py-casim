"""Nox sessions."""
import nox


@nox.session(reuse_venv=True)
def lint(session):
    session.install("flake8")
    session.run("flake8", "py_casim", "tests")


@nox.session(reuse_venv=True)
def tests(session):
    # same as pip install -r -requirements-dev.txt
    session.install("-r", "requirements-dev.txt")
    session.run("pytest")
