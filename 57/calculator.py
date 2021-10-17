import argparse
from operator import add, sub, mul, truediv
from functools import reduce

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    if operation == 'add':
        oper = add
    elif operation == 'mul':
        oper = mul
    elif operation == 'sub':
        oper = sub
    else:
        oper = truediv

    return round(reduce(oper, numbers), 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", help="increase output verbosity", nargs="*")


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    # call_calculator(stdout=True)
    create_parser()
    print(calculator('div', [2.2, 7, 1.1]))