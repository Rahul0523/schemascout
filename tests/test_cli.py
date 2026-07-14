from typer.testing import CliRunner

from schemascout.cli import app

runner = CliRunner()


def test_scan_command_runs():
    result = runner.invoke(app, ["some-dsn"])
    assert result.exit_code == 0
