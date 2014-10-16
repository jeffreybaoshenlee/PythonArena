fin=open('words1.txt')

def asb():
    res=[]
    d=dict()
    index=0
    wordlist=[]
    for line in fin:
        word=line.strip()
        wordlist.append(word)    
    a=list(wordlist[index])
    a.sort()
    for stringword in wordlist:
        t=list(stringword)
        t.sort()
        if a==t:
            res.append(stringword)
    for i in res:
        wordlist.remove(i)
    print(res)
    return wordlist[index]
print(asb())
