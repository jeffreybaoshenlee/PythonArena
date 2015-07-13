__author__ = "jeffrey"
__date__ = "$2015/7/13 下午 01:23:26$"

import unittest

class TestImport(unittest.TestCase):
    def test_all_special_attribute(self):
        import nerddata
        with self.assertRaises(AttributeError):
            print(nerddata.__all__)
        with self.assertRaises(AttributeError):
            print(nerddata.InputData.__all__)

if __name__ == "__main__":
    from mypackage import *

    a = Projectile(1.5, 3)
    b = Projectile(4, 1.7)
    after_a, after_b = simulate_collision(a, b)
    print(after_a)
    print(after_b)
    
    import mypackage
    print(mypackage.utils._dot_product)
    
    unittest.main()