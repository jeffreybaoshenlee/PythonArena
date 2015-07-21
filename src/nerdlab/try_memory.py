__author__ = "jeffrey"
__date__ = "$2015/7/21 上午 11:59:06$"

import hashlib
import os

class MyObject(object):
    def __init__(self):
        self.x = os.urandom(10000)
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