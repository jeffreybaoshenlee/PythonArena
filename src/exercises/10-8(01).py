def has_duplicates(t):
    res=[]
    index=0
    for s in t:
        if not(s in res):
            res.append(s)
        else:
            index=index+1

    return index>0
        
print(has_duplicates([1,2,3]))