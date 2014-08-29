def has_duplicates(t):
    res=[]
    index=0
    for s in t:
        if not(s in res):
            res.append(s)
        else:
            index=index+1

    return index>0

def has_duplicates_lite(t):
    foundChars=[]
    for char in t:
        if char not in foundChars:
            foundChars.append(char)
        else:
            return True

    return False

def has_duplicates_lite2(t):
    tempSet = set(t)
    print(tempSet)
    
    elementCount=len(tempSet)
    print("The length of the Set: "+str(elementCount))
    return elementCount<len(t)
        
print(has_duplicates([1,2,3]))
print(has_duplicates_lite([1,2,3]))
print(has_duplicates_lite2([1,2,3]))

print(has_duplicates([3,1,2,1,3]))
print(has_duplicates_lite([3,1,2,1,3]))
print(has_duplicates_lite2([3,1,2,1,3]))