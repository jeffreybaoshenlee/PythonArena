__author__ = "jeffrey"
__date__ = "$2015/6/3 下午 01:02:58$"

from LineCountWorker import LineCountWorker
from PathInputData import PathInputData
from threading import Thread as Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

if __name__ == "__main__":
    config = {'data_dir': "/home/jeffrey/testdir"}
    result = mapreduce(LineCountWorker, PathInputData, config)
    print(result)