from operator import add, sub, mul, truediv

ops = {"+": add, "-": sub, "*": mul, "/": truediv}


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

    Examples - input -> output:
    '2 * 3' -> 6
    '2 + 6' -> 8

    Support +, -, * and /, use "true" division (so 2/3 is .66
    rather than 0)

    Make sure you convert both numbers to ints.
    If bad data is passed in, raise a ValueError.
    """
    try:
        num1, oper, num2 = calculation.split()
        return ops[oper](int(num1), int(num2))
    except (KeyError, ValueError, ZeroDivisionError) as exc:
        print(exc)
        raise ValueError
