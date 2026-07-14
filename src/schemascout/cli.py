import typer

app = typer.Typer()


@app.command()
def scan(dsn: str = typer.Argument(..., help="Database connection string to scan")):
    """Inspect a database and generate architecture documentation."""
    typer.echo("scan: not yet implemented")


if __name__ == "__main__":
    app()
