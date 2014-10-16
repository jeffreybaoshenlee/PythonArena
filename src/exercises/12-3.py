def most_frequent(words):
    t=[]
    for word in words:
        t.append(word)
    t.sort(reverse=True)
    return t
print(most_frequent('kucs'))