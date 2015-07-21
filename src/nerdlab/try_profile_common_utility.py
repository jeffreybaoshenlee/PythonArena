__author__ = "jeffrey"
__date__ = "$2015/7/21 上午 10:57:59$"

import time

def my_utility(a, b):
    time.sleep(a / 100000.0 + b / 1000000.0)

def first_func():
    for _ in range(1000):
        my_utility(4, 5)

def second_func():
    for _ in range(10):
        my_utility(1, 3)

def my_program():
    for _ in range(20):
        first_func()
        second_func()

if __name__ == "__main__":
    from nerdprofile import run_profiler
    profiler = run_profiler(my_program)
    
    from nerdprofile import print_stats
    print_stats(profiler,True)