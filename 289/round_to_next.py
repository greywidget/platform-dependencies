from math import ceil


def round_to_next(number: int, multiple: int):
    return ceil(number / multiple) * multiple


if __name__ == "__main__":
    print(round_to_next(-10, -10))
