from typer.testing import CliRunner

from schemascout.cli import app

runner = CliRunner()


def test_scan_command_runs(tmp_path):
    dsn = str(tmp_path / "some-dsn.db")
    result = runner.invoke(app, [dsn])
    assert result.exit_code == 0
