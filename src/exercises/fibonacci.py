from util.Number import *

while(True):
    val = input("Enter a positive integer, negative or other to exit: ")
    
    try:
        num = int(val)
    except ValueError:
        break;
        
    if num>=0:    
        print (fibonacci(num))
    else:
        break

print("Exit")