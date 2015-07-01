__author__ = "jeffrey"
__date__ = "$2015/7/1 下午 05:26:40$"


from concurrent.futures import *
from nerdmath import *
from nerdtest import *

numbers = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2039045, 2020802)]

@get_result_and_print_time
def make_list():
    return list(map(gcd, numbers))

@get_result_and_print_time
def make_list_using_thread_pool():
    pool = ThreadPoolExecutor(max_workers=4)
    return list(pool.map(gcd, numbers))

@get_result_and_print_time
def make_list_using_process_pool():
    pool = ProcessPoolExecutor(max_workers=4)
    return list(pool.map(gcd, numbers))

if __name__ == "__main__":
    print(make_list())
    print(make_list_using_thread_pool())
    print(make_list_using_process_pool())