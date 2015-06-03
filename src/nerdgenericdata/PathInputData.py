__author__ = "jeffrey"
__date__ = "$2015/6/3 下午 12:50:50$"

from GenericInputData import GenericInputData

class PathInputData(GenericInputData):
    
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()
    
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        
        import os
        for name in os.listdir(data_dir):
            path = os.path.join(data_dir, name)
            if not os.path.isdir(path):
                yield cls(path)