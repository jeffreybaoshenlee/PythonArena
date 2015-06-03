__author__ = "jeffrey"
__date__ = "$2015/6/3 下午 12:51:32$"

class Worker(object):

    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError