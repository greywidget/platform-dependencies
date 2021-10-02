from functools import wraps


def make_html(element):
    def middle(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f"<{element}>{func(*args, **kwargs)}</{element}>"

        return wrapper

    return middle
