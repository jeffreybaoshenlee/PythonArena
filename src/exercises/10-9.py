def remove_duplicates(t):
    res=[]
    for s in t:
        if not(s in res[:]):
            res.append(s)        
    print(res)
    return res
remove_duplicates(['a','a','b','a','a','b','s','u','c','k'])
