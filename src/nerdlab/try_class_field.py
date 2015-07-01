__author__ = "jeffrey"
__date__ = "$2015/6/8 下午 04:59:17$"

class MyClass(object):
    def __init__(self):
        self.field0 = 'field0'
        self.field1_ = 'field1'
        self.field2__ = 'field2'
        self.field3___ = 'field3'
        
        self._field4 = 'field4'
        self._field5_ = 'field5'
        self._field6__ = 'field6'
        self._field7___ = 'field7'
        
        self.__field8 = 'field8'
        self.__field9_ = 'field9'
        self.__field10__ = 'field10'
        self.__field11___ = 'field11'
        
        self.___field12 = 'field12'
        self.___field13_ = 'field13'
        self.___field14__ = 'field14'
        self.___field15___ = 'field15'

if __name__ == "__main__":
    my_obj = MyClass()
    
    import pprint
    pprint.pprint(my_obj.__dict__)
