def rotate_word(word,number):
    result=[]
    for char in word:
        encrypted_char=ord(char)+number
        result.append(chr(encrypted_char))
        
    return ''.join(result)

encrypted_word=rotate_word('cheer',7)
print(encrypted_word)