#! /usr/bin/python

__author__ = "jeffrey"
__date__ = "$2015/5/22 下午 03:21:13$"

def test_scoping_workaround():
    var = 100
    var_list = [11, 12, 13, 14, 15]
    
    def inner_func():
        var = 200
        
        #If you use this workaround, you must not create the variable of the 
        #   same name in the inner scope.
        #var_list = [9,10]
        
        #Hacking: Assign the 0th element of the var_list instead of directly 
        #   assigning a list itself like the commented out statement above.
        #   var_list[0] is an access to the var_list plus an assignment to its
        #   0th element, not a pure assignment like var_list, so when accessing
        #   the var_list, Python must use socpe traversal rules to search for 
        #   var_list in the outer scope.
        var_list[0] = 5
        print("Inner var: "+str(var))
        
    inner_func()
    
    print ("var :" + str(var))
    print ("var_list :"+str(var_list))

if __name__ == "__main__":
    test_scoping_workaround()
