__author__ = "jeffrey"
__date__ = "$2015/6/3 下午 01:02:58$"

from LineCountWorker import LineCountWorker
from PathInputData import PathInputData
import os
from threading import Thread as Thread

def generate_inputs(data_dir):    
    for name in os.listdir(data_dir):
        path = os.path.join(data_dir, name)
        if not os.path.isdir(path):
            yield PathInputData(path)

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers
    
def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

if __name__ == "__main__":
    dir_name = "/home/jeffrey/testdir"
        
    result = mapreduce(dir_name)
    print(result)