def middle(source_list):
    result = []
    length=len(source_list)
    
    for index in range(1,length-1):
        element = source_list[index]
        result.append(element)
        
    return result;

def is_sorted(testee):
    length = len(testee)
    
    for index in range(0,length-1):
        this_element=testee[index]
        next_element=testee[index+1]
        if (this_element>next_element):
            return False
        
    return True