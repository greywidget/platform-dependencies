import pytest
from script import app
from typer.testing import CliRunner


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_app(runner):
    result = runner.invoke(app, "Boris")
    assert result.exit_code == 0
    assert "Hello Boris" in result.stdout


def test_help(runner):
    result = runner.invoke(app, "--help")
    assert result.exit_code == 0
    assert "The name of the person to greet" in result.stdout
