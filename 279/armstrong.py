def is_armstrong(n: int) -> bool:
    chars = list(str(n))
    power = len(chars)
    return n == sum([int(item) ** power for item in chars])


if __name__ == "__main__":
    print(is_armstrong(371))
