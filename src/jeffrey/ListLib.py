def middle(source_list):
    result = []
    length=len(source_list)
    if (length < 2):
        print("The list must have at least two elements.")
        return result
    
    for index in range(1,length-1):
        element = source_list[index]
        result.append(element)
        
    return result;