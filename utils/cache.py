import functools
import time

_cache = {}

def cache(expiration=60):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, tuple(kwargs.items()))
            if key in _cache:
                result, timestamp = _cache[key]
                if time.time() - timestamp < expiration:
                    return result
            result = func(*args, **kwargs)
            _cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator

def clear_cache():
    _cache.clear()
