__author__ = "jeffrey"
__date__ = "$2015/7/17 上午 11:40:28$"

import unittest

class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class BetterClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)

class TestRepr(unittest.TestCase):
    def test_normal_class(self):
        obj = OpaqueClass(1, 2)
        print(obj)

        repr_str = repr(obj)
        print(repr_str)

        with self.assertRaises(SyntaxError):
            eval(repr_str)

    def test_better_class(self):
        obj = BetterClass(1, 2)
        print(obj)
        
        repr_str = repr(obj)
        print(repr_str)
        
        self.assertEqual(obj, eval(repr_str))
        
if __name__ == "__main__":
    unittest.main()