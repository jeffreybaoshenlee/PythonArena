def has_duplicates(t):
    inverse=dict()
    for key in t:
        if key not in t:
            inverse[key]=1
        else:
            return True
h=has_duplicates('parrot')
print(h)
def has_duplicates2(t):
    a=set(t)
    print(a)
    return len(set(t))<len(t)
a=has_duplicates([1,2,3])
print(a)