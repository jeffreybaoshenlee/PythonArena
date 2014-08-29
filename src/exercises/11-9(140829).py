def has_duplicates(t):
    found=dict()
    for element in t:
        if element in found:
            return True
        else:
            found[element]=1
    
    return False
        
result=has_duplicates('parrot')
print(result)

result=has_duplicates([1,2,3])
print(result)