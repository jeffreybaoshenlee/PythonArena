__author__ = "jeffrey"
__date__ = "$2015/7/3 下午 06:20:29$"

class MyClass():
    def __init__(self):
        self._my_field = 5
        print("Constructor called.")

if __name__ == "__main__":
    my_obj = MyClass()
    print(my_obj._my_field)
    
    from os.path import expanduser
    file_path = expanduser("~") + '/桌面/state.bin'
    
    import pickle
    with open(file_path, 'wb') as file:
        pickle.dump(my_obj, file)
    with open(file_path, 'rb') as file:
        my_restored_obj = pickle.load(file)
        
    print(my_restored_obj.__dict__)