result={0:0,1:1}

def fibonacci(n):
    query = result.get(n)
    if query is not None:
        return query
    else:
        result[n] = fibonacci(n-1)+fibonacci(n-2)
        return result[n]

if __name__=='__main__':
    for i in range(0,10):
        print(fibonacci(i))