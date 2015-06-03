__author__ = "jeffrey"
__date__ = "$2015/6/3 下午 12:48:58$"

class GenericInputData(object):

    def read(self):
        raise NotImplementedError
    
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError