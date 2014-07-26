import WordCheckLib

is_palindrome=WordCheckLib.is_palindrome_no_debug

for testee in range(100000,999996):
    lastFourDigits = str(testee)[2:]
    if not is_palindrome(lastFourDigits):
        continue
        
    nextNumber = testee+1
    lastFiveDigits = str(nextNumber)[1:]
    if not is_palindrome(lastFiveDigits):
        continue
        
    nextNumber = testee+2
    middleFourDigits=str(nextNumber)[1:5]
    if not is_palindrome(middleFourDigits):
        continue
        
    nextNumber = testee+3
    allSixDigits = str(nextNumber)
    if is_palindrome(allSixDigits):
        print(testee)