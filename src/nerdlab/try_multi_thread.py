__author__ = "jeffrey"
__date__ = "$2015/6/23 下午 02:00:48$"

from nerdmath import *
from threading import Thread

class FactorizeThread(Thread):

    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

if __name__ == "__main__":
    numbers = [2139079, 1214759, 1516637, 1852285, 2139079, 1214759, 1516637, 1852285]
    threads = []
    
    from time import time
    start = time()

    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

    end = time()
    print('Took %.3f seconds' % (end - start))