class IOManipulator(object):
    def __init__(self,function=None):
       self.function=function
       
    def do(self,output):
       self.function(output)
       
def do_endl(stream):
    stream.output.write('\n')
    stream.output.flush()
   
endl=IOManipulator(do_endl)