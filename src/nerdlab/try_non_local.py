#! /usr/bin/python

def test_non_local():
    local_var = 1
    def closure_fun():
        a = 5
        b = 10
        #The variable modified by the nonlocal keyword must be exist in the 
        #   enclosing function.
        #nonlocal var1
        #The variable to be modified by nonlocal cannot be assigned or used  
        #   before nonlocal declaration.
        #local_var = 2
        #print(local_var)
        nonlocal local_var
        local_var = a + b
        print(local_var)

    closure_fun()
    
    #Even the closure function modifies a variable of current function as 
    #   nonlocal, we cannot access it in the current function.
    #return var1
    return local_var

__author__ = "jeffrey"
__date__ = "$2015/5/22 下午 02:40:49$"

if __name__ == "__main__":
    print(test_non_local())