def round_to_next(number: int, multiple: int):
    remainder = number % multiple

    if remainder == 0:
        return number

    return number + multiple - remainder


if __name__ == "__main__":
    print(round_to_next(-10, -10))
