#! /usr/bin/python

global_var = 10

def test_global():
    global global_var
    global_var = 100
    print(global_var)
    
def test_global_with_same_name():
    global_var = 200
    print(global_var)

__author__ = "jeffrey"
__date__ = "$2015/5/22 下午 02:58:18$"

if __name__ == "__main__":
    test_global()
    test_global_with_same_name()
