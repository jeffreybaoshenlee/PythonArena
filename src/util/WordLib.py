def rotate_word_bug(word,number):
    result=[]
    for char in word:
        encrypted_char=ord(char)+number
        result.append(chr(encrypted_char))
        
    return ''.join(result)

def rotate_word(word,number):
    if number<0 or number>=26:
        return word
    
    result=[]
    for char in word:
        encrypted_char=ord(char)+number
        
        ord_z=ord('z')        
        if (encrypted_char>ord_z):
            encrypted_char=encrypted_char-26
        
        result.append(chr(encrypted_char))
        
    return ''.join(result)

if __name__ == '__main__':
    print(rotate_word_bug('zigzag',12))
    print(rotate_word('zigzag',12))
    print(rotate_word_bug('a',26))
    print(rotate_word('a',26))