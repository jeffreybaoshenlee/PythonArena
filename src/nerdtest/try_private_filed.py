__author__ = "jeffrey"
__date__ = "$2015/6/8 下午 05:58:06$"

class MyClass(object):
    def __init__(self, value):
        self.__value = value
        
    def get_value(self):
        return str(self.__value)

class MyIntegerSubclass(MyClass):
    def get_value(self):
#        return int(self._MyClass__value)
        return int(super().get_value())

if __name__ == "__main__":
    my_obj = MyClass(12)
    assert my_obj.get_value() == '12'
    
    my_int = MyIntegerSubclass(25)
    assert my_int.get_value() == 25