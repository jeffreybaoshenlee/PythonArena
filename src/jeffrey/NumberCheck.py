from WordCheckLib import *

for testee in range(100000,999996):
    lastFourDigits = str(testee)[2:]
    if not is_palindrome_no_debug(lastFourDigits):
        continue
        
    nextNumber = testee+1
    lastFiveDigits = str(nextNumber)[1:]
    if not is_palindrome_no_debug(lastFiveDigits):
        continue
        
    nextNumber = testee+2
    middleFourDigits=str(nextNumber)[1:5]
    if not is_palindrome_no_debug(middleFourDigits):
        continue
        
    nextNumber = testee+3
    allSixDigits = str(nextNumber)
    if is_palindrome_no_debug(allSixDigits):
        print(testee)      