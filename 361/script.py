import typer
from rich.console import Console
from rich.table import Column, Table

app = typer.Typer()

console = Console()


@app.command()
def table():
    table = Table(
        Column(header="Name"),
        Column(header="Favorite Tool/Framework"),
    )
    table.add_row("Bob", "Vim")
    table.add_row("Julian", "Flask")
    table.add_row("Robin", "VS Code")
    console.print(table)


if __name__ == "__main__":
    app()
