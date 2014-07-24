def is_palindrome(word):
    length = len(word)
    middlePoint = int(length/2)
    round = 0
    
    for frontIndex,backIndex in zip(range(0,middlePoint), range (length-1,middlePoint,-1)):
        frontLetter = word[frontIndex]
        backLetter = word[backIndex]
        print("Test round "+str(round)+": "+frontLetter+", "+backLetter)
        if (frontLetter!=backLetter):
            print("Test failed.")
            return False
        round+=1
        
    return True
        
for testee in ["rotator","lol","meow"]:
    result = is_palindrome(testee)
    print(result)
    print()