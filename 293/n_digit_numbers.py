import math
from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    result = []
    for item in numbers:
        if item == 0:
            result.append(item)
        else:
            power = math.floor(math.log10(abs(item)) + 1)
            result.append(int(item * 10 ** (n - power)))

    return result


if __name__ == "__main__":
    print(
        n_digit_numbers(
            [0, 1, 2, 3],
            2,
        )
    )
