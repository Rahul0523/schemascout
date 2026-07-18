---
name: scan-schema
description: Runs SchemaScout's scan command against a given SQLite database file and reports the tables and columns found. Use when the user wants to inspect/scan a database file, list its tables, or see its schema.
---

# Scan Schema

Runs SchemaScout's `scan` command against a database file and reports the
tables and columns it finds.

## When to use this skill

Use when the user asks to scan, inspect, or list the schema/tables/columns
of a database file (e.g. "scan sample.db", "what tables are in this
database?").

## Steps

1. Confirm the database file path. If the user didn't give one, ask for it
   or look for a `*.db` file in the working directory.
2. Verify the file exists before running the scan:
   ```bash
   ls -la <path-to-db-file>
   ```
3. Run the scan command via `uv run`:
   ```bash
   uv run schemascout <path-to-db-file>
   ```
4. Report the results back to the user as a concise summary: number of
   tables found, and for each table, its name and columns. If the command
   reports "No tables found.", say so plainly rather than treating it as an
   error.

## Notes

- SchemaScout currently connects to the DSN as a SQLite file path (see
  `src/schemascout/db/connection.py`) — pass a path to a `.db`/`.sqlite`
  file, not a full connection URL.
- If the command raises an error (e.g. file doesn't exist or isn't a valid
  SQLite database), surface the error message to the user instead of
  guessing at the schema.
