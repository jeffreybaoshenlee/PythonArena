__author__ = "jeffrey"
__date__ = "$2015/7/21 上午 11:59:06$"

import hashlib
import os

class MyObject(object):
    def __init__(self):
        self.x = os.urandom(20000)
        self.y = hashlib.sha1(self.x).hexdigest()

def get_data():
    values = []
    for _ in range(50):
        obj = MyObject()
        values.append(obj)
    return values

def run():
    deep_values = []
    for _ in range(50):
        deep_values.append(get_data())
    return deep_values

if __name__ == "__main__":
    import gc
    found_objects = gc.get_objects()
    print('%d objects before' % len(found_objects))


    x = run()
    found_objects = gc.get_objects()
    print('%d objects after' % len(found_objects))
    for obj in found_objects[:3]:
        print(repr(obj)[:100])
    
    import tracemalloc
    tracemalloc.start(10) # Save up to 10 stack frames

    time1 = tracemalloc.take_snapshot()
    x = run()
    time2 = tracemalloc.take_snapshot()
    stats = time2.compare_to(time1, 'lineno')
 
    for stat in stats:
        print(stat)
        
    stats = time2.compare_to(time1, 'traceback')
    top = stats[0]
    print('\n'.join(top.traceback.format()))