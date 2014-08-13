from util.WordCountLib import *

def print_hist(histogram):
    key_list = histogram.keys()
    
    key_list=list(key_list)
    key_list.sort()

    for character in key_list:
        print(character, histogram[character])
        
my_histogram=histogram('brontosaurus')
print_hist(my_histogram);