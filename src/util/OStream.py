from util.IOManipulator import *

class OStream(object):
    def __init__(self,output=None):
       if output is None:
           import sys
           output=sys.stdout
           self.output=output
           self.format='%s'
           
    def __lshift__(self,thing):
       if  isinstance(thing,IOManipulator):
           thing.do(self)
       else:
           self.output.write(self.format % thing)
           self.format='%s'
       return self
   
def example_main():
   cout=OStream()
   cout << "The average of " << 1 << " and " << 3 << " is "<<(1+3)/2 << endl
   
if __name__=='__main__':
    example_main()