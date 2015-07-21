__author__ = "jeffrey"
__date__ = "$2015/7/21 上午 09:31:35$"

def insertion_sort(data, insert_value_func):
    result = []
    for value in data:
        insert_value_func(result, value)
    return result

def linear_insertion_sort(data):
    return insertion_sort(data, linear_insert_value)

def linear_insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)

def bisect_insertion_sort(data):
    return insertion_sort(data, bisect_insert_value)

def bisect_insert_value(array, value):
    from bisect import bisect_left

    i = bisect_left(array, value)
    array.insert(i, value)

if __name__ == "__main__":
    max_value = 10 ** 4
    from random_tool import gen_random_numbers
    data = gen_random_numbers(max_value)

    from nerdprofile import run_profiler
    profiler = run_profiler(linear_insertion_sort, data)
    
    from nerdprofile import print_stats
    print_stats(profiler)
    
    data = gen_random_numbers(max_value)
    profiler = run_profiler(bisect_insertion_sort, data)
    print_stats(profiler)