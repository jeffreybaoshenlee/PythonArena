from util.WordLib import *

def found_rotate_pair(vocabulary,rotate_len):
    result=dict()
    for word in vocabulary:
        rotated_word=rotate_word(word,rotate_len)
        
        if rotated_word in vocabulary:
            result[word]=rotated_word
            
    return result

vocabulary=['cc','dd','aa','bb','cat','dbu','melon','nfmpo','my','your']
print(found_rotate_pair(vocabulary,1))
print(found_rotate_pair(vocabulary,2))
print(found_rotate_pair(vocabulary,3))