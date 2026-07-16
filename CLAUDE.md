# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

SchemaScout is a CLI tool that explores undocumented SQL databases and generates architecture documentation. Point it at a database and it inspects tables, relationships, and constraints to produce human-readable docs describing the schema.

The project is an early-stage scaffold: the CLI entry point and DB connection module exist but are not yet implemented (`scan` just echoes a placeholder; `connect` raises `NotImplementedError`).

## Commands

This project uses `uv` for dependency management (see `uv.lock`) and `hatchling` as the build backend.

```bash
# Install dependencies (including dev group)
uv sync

# Run the CLI
uv run schemascout <dsn>

# Run tests
uv run pytest

# Run a single test
uv run pytest tests/test_cli.py::test_scan_command_runs
```

## Tooling rationale

- **uv over Poetry/pip** — single fast binary for dependency resolution, virtualenv management, and running scripts (`uv run`), with a lockfile (`uv.lock`) for reproducible installs. Avoids Poetry's slower resolver and pip's lack of built-in lockfile/venv management.
- **Typer over Click/argparse** — CLI commands are plain type-hinted functions (`@app.command()`), so argument parsing, validation, and `--help` text are derived from function signatures instead of hand-written parser boilerplate. Built on Click, so Click's ecosystem is still available if needed.
- **pytest** — standard choice for Python testing; supports Typer's `CliRunner` for in-process CLI invocation, fixtures, and concise assertion syntax without the boilerplate of `unittest`.

## Architecture

- `src/schemascout/cli.py` — Typer app and CLI entry point (`schemascout` console script, registered in `pyproject.toml`). Commands are added here as Typer `@app.command()` functions.
- `src/schemascout/db/connection.py` — owns opening/managing the connection to the target SQL database being scanned; called with the DSN passed to the CLI.
- Package uses the src-layout (`src/schemascout/`), packaged via `[tool.hatch.build.targets.wheel] packages = ["src/schemascout"]`.
- Tests use Typer's `CliRunner` (`typer.testing.CliRunner`) to invoke the CLI in-process rather than as a subprocess.
