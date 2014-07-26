def middle(source_list):
    result = []
    length=len(source_list)
    
    for index in range(1,length-1):
        element = source_list[index]
        result.append(element)
        
    return result;