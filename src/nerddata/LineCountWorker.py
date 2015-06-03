__author__ = "jeffrey"
__date__ = "$2015/6/3 下午 12:52:32$"

from Worker import Worker

class LineCountWorker(Worker):

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result