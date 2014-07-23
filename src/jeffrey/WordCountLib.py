def count_word(filename, lowestWordLength):
    fin=open(filename)
    
    count=0
    for line in fin:
        if (len(line)>=lowestWordLength):
            print("Found a line whose lenght is at least "+str(lowestWordLength)+":")
            print(line)
            count=count+1
            
    return count

def count_word_without(filename, letterToExclude):
    fin=open(filename)
    
    count=0
    for line in fin:
        if (letterToExclude not in line):
            print("Found a line without letter \""+letterToExclude+"\" :")
            print(line)
            count=count+1
    
    return count

filename= 'words.txt'
minimumLength=21
result = count_word(filename,minimumLength);
print("The number of the words whose length is at least "+str(minimumLength)+" is: "+str(result))

letterToExclude='e'
result = count_word_without(filename,letterToExclude);
print("The number of the words without the letter \""+letterToExclude+"\" is: "+str(result))