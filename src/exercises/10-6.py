def is_sorted(t):
    res=[]
    index=0
    for x in t:
        res.append(x)
    a=res[:]
    b=res[1:]
    for i in range(0,len(b)):
        if a[index]<b[index] or a[index]==b[index]:
            index=index+1
        else:
            print('suck')
            return False
    print('true')
is_sorted(['b','a'])    