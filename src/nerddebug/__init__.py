__author__ = "jeffrey"
__date__ = "$2015/7/2 下午 05:17:03$"

from functools import *

def trace(func):
    @wraps(func)
    def wrapper(*args, ** kwargs):
        result = func(*args, ** kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper

if __name__ == '__main__':
    from nerdmath import *
    print(fibonacci(3))
    print(fibonacci)
    help(fibonacci)