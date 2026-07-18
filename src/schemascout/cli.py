import typer

from schemascout.db.connection import connect, list_tables

app = typer.Typer()


@app.command()
def scan(dsn: str = typer.Argument(..., help="Database connection string to scan")):
    """Inspect a database and generate architecture documentation."""
    conn = connect(dsn)
    tables = list_tables(conn)

    if not tables:
        typer.echo("No tables found.")
        return

    for table_name, columns in tables.items():
        typer.echo(f"{table_name}")
        for column in columns:
            typer.echo(f"  - {column}")


if __name__ == "__main__":
    app()
