from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:

    cache_store = {}

    @wraps(func)
    def wrapper(*args):
        key = args
        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]
        print("Calculating new result")
        result = func(*args)
        cache_store[key] = result
        return result

    return wrapper
