from functools import lru_cache


@lru_cache
def cached_fib(n):
    if 0 <= n <= 1:
        return n

    return cached_fib(n - 2) + cached_fib(n - 1)
