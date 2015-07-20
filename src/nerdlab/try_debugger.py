__author__ = "jeffrey"
__date__ = "$2015/7/20 上午 11:22:29$"

def complex_func(a, b, c):
    a = a + 1
    b *= 2
    c -= 3
    
    import pdb;pdb.set_trace()
    
    print(a)
    foo(a)
    print(b)
    print(c)
    return (a, b, c)

def foo(a):
    a = a + 10
    return a

if __name__ == "__main__":
    import random
    args = [random.randint(0, 100) for _ in range(0, 3)]
    print(args)
    a, b, c = complex_func(*args)
    import pdb;pdb.set_trace()
    print(a + b + c)