def rotate_word(word,number):
    res=[]
    for a in word:
        b=ord(a)+number
        res.append(chr(b))
    return res
h=rotate_word('cheer',7)
print(h)