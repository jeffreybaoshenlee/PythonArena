def bisect(word,t):
    word.sort()
    print(word)
    print(len(word))
    i=int(len(word)/2)
    print(i)

    if i>0:
        if word[i]==t:
            print('True')
            print(word[i])
            return word[i]
        elif word[i]>t:
            return bisect(word[:i],t)
        else:
            return bisect(word[i:],t)        
    print('suck')    
    return False

bisect([1,3,4,6,78,4,5,8,9,12,14,15,17,99,123,56,34,34,67,78,89,90,4],99)        