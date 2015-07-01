__author__ = "jeffrey"
__date__ = "$2015/7/1 下午 05:30:49$"

import time

def get_result(testee, run_time_needed):
    def wrapper(*args, ** kwargs):
        start = time.time()
        result = testee(*args, ** kwargs)
        end = time.time()
        run_time = end - start
        print(testee.__name__ + ' took %.3f seconds' % run_time)
        if run_time_needed:
            return result, run_time
        else:
            return result
    return wrapper

def get_result_and_run_time(testee):
    return get_result(testee, True)

def get_result_and_print_time(testee):
    return get_result(testee, False)