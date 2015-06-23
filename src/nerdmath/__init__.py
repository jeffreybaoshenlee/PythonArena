__author__ = "jeffrey"
__date__ = "$2015/6/23 下午 01:53:19$"

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

if __name__ == '__main__':
    numbers = [2139079, 1214759, 1516637, 1852285, 2139079, 1214759, 1516637, 1852285]
    
    from time import time
    start = time()
    for number in numbers:
        list(factorize(number))
    end = time()

    print('Took %.3f seconds' % (end - start))