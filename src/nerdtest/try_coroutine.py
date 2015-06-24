__author__ = "jeffrey"
__date__ = "$2015/6/24 下午 03:41:11$"

def double_fun():
    x = 5
    while True:
        x = yield x * 2
        print("Coroutine's loop executed")
        print('Current x: {:d}'.format(x))

def double_fun_two_step():
    x = 5
    while True:
        result = x * 2
        x = (yield result)
        print("Coroutine's loop executed")
        print('Current x: {:d}'.format(x))

if __name__ == "__main__":
    gen = double_fun_two_step()
    print("Genertator ready.")
    print(gen.send(None))
    print("None sent.")
    print(gen.send(9))
    print("9 sent.")
    print(gen.send(100))
    print("100 sent.")