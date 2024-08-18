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
