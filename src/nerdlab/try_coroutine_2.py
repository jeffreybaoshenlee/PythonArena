__author__ = "jeffrey"
__date__ = "$2015/6/24 下午 03:41:11$"

def minimize():
    current = yield
    print("Entering while")
    while True:
        print("Before yield")
        value = yield current
        print("After yield")
        current = min(value, current)

if __name__ == "__main__":
    it = minimize()
    print("Preparing")
    next(it)
    print("Sending 10")
    print(it.send(10))
    print("Sending 4")
    print(it.send(4))
    print("Sending 22")
    print(it.send(22))
    print("Sending -1")
    print(it.send(-1))