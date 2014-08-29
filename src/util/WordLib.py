def rotate_word(word,number):
    result=[]
    for char in word:
        encrypted_char=ord(char)+number
        result.append(chr(encrypted_char))
        
    return ''.join(result)