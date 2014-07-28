def is_palindrome(word):
    length = len(word)
    middlePoint = int(length/2)
    round = 0
    
    for frontIndex,backIndex in zip(range(0,middlePoint), range (length-1,middlePoint-1,-1)):
        frontLetter = word[frontIndex]
        backLetter = word[backIndex]
        print("Test round "+str(round)+": "+frontLetter+", "+backLetter)
        if (frontLetter!=backLetter):
            print("Test failed.")
            return False
        round+=1
        
    return True

def is_palindrome_no_debug(word):
    length = len(word)
    middlePoint = int(length/2)
    
    for frontIndex,backIndex in zip(range(0,middlePoint), range (length-1,middlePoint-1,-1)):
        frontLetter = word[frontIndex]
        backLetter = word[backIndex]
        if (frontLetter!=backLetter):
            return False
        
    return True

def is_palindrome_gentle(word):
    length = len(word)
    frontIndex=0
    backIndex=length-1
    
    while frontIndex<backIndex:
        frontLetter = word[frontIndex]
        backLetter = word[backIndex]
        
        if (frontLetter!=backLetter):
            return False
        
        frontIndex+=1;
        backIndex-=1;
    return True

if __name__ == '__main__':
    for testee in ["rotator","lol","meow","blob"]:
        result = is_palindrome(testee)
        print(result)
        print()
        
    for testee in ["rotator","lol","meow","blob"]:
        result = is_palindrome_gentle(testee)
        print(result)
        print()