#! /usr/bin/python

__author__ = "jeffrey"
__date__ = "$2015/5/20 下午 01:10:47$"

#def test_try_else(value_to_test, stadard_value):
#    try:
#        if (value_to_test != stadard_value):
#            raise ValueError("These two values are unequal.")
#    # Trying: If you use else in the try compound statement, you must write 
#    #           the except block.
#    else:
#        print("These two values are equal.")
        
def test_try_except_else(value_to_test, stadard_value):
    try:
        if (value_to_test != stadard_value):
            raise ValueError("These two values are unequal.")
    except ValueError as e:
        raise RuntimeError from e
    else:
        print("These two values are equal.") 


def test_try_except_else_finally(value_to_test, stadard_value):
    try:
        if (value_to_test != stadard_value):
            raise ValueError("These two values are unequal.")
    except ValueError as e:
        raise RuntimeError from e
    else:
        print("These two values are equal.") 
    finally:
        print("Completed.") 

if __name__ == "__main__":
    print("Testing test_try_except_else ...")
    
    try:
        test_try_except_else(1, 1)
        test_try_except_else(1, 2)
    except BaseException as e:
        print (e.__cause__)
    
    print("Testing test_try_except_else_finally ...")
        
    test_try_except_else_finally(1, 1)
    test_try_except_else_finally(1, 2)