def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = 0
    except TypeError as e:
        raise e

    if result < 0:
        raise ValueError

    return result
