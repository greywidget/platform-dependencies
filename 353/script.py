import typer  # use typer.run and typer.Argument


def sum_numbers(a: int, b: int):
    """Sums two numbers"""
    return a + b


def main(
    num1: int = typer.Argument(..., help="The value of the first summand"),
    num2: int = typer.Argument(..., help="The value of the second summand"),
):
    """
    CLI that allows you to add two numbers
    """
    print(sum_numbers(num1, num2))


if __name__ == "__main__":
    typer.run(main)
