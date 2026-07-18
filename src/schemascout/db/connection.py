# Opens and manages the connection to the target SQL database being scanned.

import sqlite3


def connect(dsn: str) -> sqlite3.Connection:
    return sqlite3.connect(dsn)


def list_tables(conn: sqlite3.Connection) -> dict[str, list[str]]:
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
    )
    table_names = [row[0] for row in cursor.fetchall()]

    tables = {}
    for table_name in table_names:
        columns = conn.execute(f'PRAGMA table_info("{table_name}")').fetchall()
        tables[table_name] = [column[1] for column in columns]
    return tables
