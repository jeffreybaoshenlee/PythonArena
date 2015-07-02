__author__ = "jeffrey"
__date__ = "$2015/6/23 下午 01:53:19$"

from nerddebug import *

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

if __name__ == '__main__':
    numbers = [2139079, 1214759, 1516637, 1852285, 2139079, 1214759, 1516637, 1852285]
    
    from time import time
    start = time()
    for number in numbers:
        list(factorize(number))
    end = time()

    print('Took %.3f seconds' % (end - start))