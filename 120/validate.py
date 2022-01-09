from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args):
        for item in args:
            if not isinstance(item, int):
                raise TypeError(f"{item} is not an int")
            if item < 0:
                raise ValueError(f"{item} is < 0")
        return func(*args)

    return wrapper
