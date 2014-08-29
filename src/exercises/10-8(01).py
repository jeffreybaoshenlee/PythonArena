def has_duplicates(t):
    res=[]
    index=0
    for s in t:
        if not(s in res):
            res.append(s)
        else:
            index=index+1
    if index>0:
        print('suck')
        return True
    else:
        print(res)
has_duplicates([1,2,3])        