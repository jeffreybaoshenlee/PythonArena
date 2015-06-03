__author__ = "jeffrey"
__date__ = "$2015/6/3 下午 12:50:50$"

from InputData import InputData

class PathInputData(InputData):
    
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()