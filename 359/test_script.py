import pytest
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_subtract(runner):
    result = runner.invoke(app, ["subtract", "7", "3"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "The delta is 4"


def test_subtract_help(runner):
    result = runner.invoke(app, ["subtract", "--help"])
    assert result.exit_code == 0
    assert "Command that allows you to add two numbers" in result.stdout


def test_subtract_a_help(runner):
    result = runner.invoke(app, ["subtract", "a", "--help"])
    assert result.exit_code == 0
    assert "The value of the first summand" in result.stdout


def test_subtract_b_help(runner):
    result = runner.invoke(app, ["subtract", "b", "--help"])
    assert result.exit_code == 0
    assert "The value of the second summand" in result.stdout


def test_compare_not_greater(runner):
    result = runner.invoke(app, ["compare", "7", "3"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "d=3 is not greater than c=7"


def test_compare_greater(runner):
    result = runner.invoke(app, ["compare", "7", "22"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "d=22 is greater than c=7"


def test_compare_equal(runner):
    result = runner.invoke(app, ["compare", "7", "7"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "d=7 is not greater than c=7"


def test_compare_help(runner):
    result = runner.invoke(app, ["compare", "--help"])
    assert result.exit_code == 0
    assert (
        "Command that checks whether a number d is greater than a number c"
        in result.stdout
    )


def test_compare_c_help(runner):
    result = runner.invoke(app, ["compare", "c", "--help"])
    assert result.exit_code == 0
    assert "First number to compare against" in result.stdout


def test_compare_d_help(runner):
    result = runner.invoke(app, ["compare", "c", "--help"])
    assert result.exit_code == 0
    assert "Second number that is compared against first number" in result.stdout
