import typer
from typing_extensions import Annotated


def sum_numbers(a: int, b: int):
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
    c: Annotated[int, typer.Option(help="Optional third value.")] = None,
):
    """CLI that allows you to add two numbers"""
    a_plus_b = sum_numbers(a, b)
    output = f"The sum is {a_plus_b} "
    if c:
        comparison = "is smaller" if c < a_plus_b else "is not smaller"
        output += f"and c {comparison}"
    else:
        output += "and c is None"
    print(output)


if __name__ == "__main__":
    typer.run(main)
