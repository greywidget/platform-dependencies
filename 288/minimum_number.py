from typing import List


def minimum_number(digits: List[int]) -> int:
    unique = sorted(set(digits)) if digits else {0}
    cunique = [str(item) for item in unique]
    return int("".join(cunique))


if __name__ == "__main__":
    print(minimum_number([4, 2, 7, 2, 99]))
    print(minimum_number([]))
