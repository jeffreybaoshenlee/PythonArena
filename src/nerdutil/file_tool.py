__author__ = "jeffrey"
__date__ = "$2015/5/12 下午 03:36:22$"

def write_random_data():
    import os
    with open('./random.bin', 'w') as file:
        file.write(os.urandom(10))
        
def write_random_binary_data():
    import os
    with open('./random.bin', 'wb') as file:
        file.write(os.urandom(10))

if __name__ == "__main__":
#    write_random_data()
    write_random_binary_data()