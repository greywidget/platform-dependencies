import typer

# The newer Annotated version passes locally, but not on the Pybites platform,
# so I had to revert to the older syntax

app = typer.Typer()


@app.command()
def main(
    name: str,
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
):
    print(f"Hello {name}. Doing something very secure with password.")
    print(f"...just kidding, here it is, very insecure: {password}")


if __name__ == "__main__":
    app()
