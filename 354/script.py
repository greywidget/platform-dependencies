import typer


def sum_numbers(a: int, b: int):
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
    c: int = typer.Option(default=None, help="The value of the second summand"),
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
