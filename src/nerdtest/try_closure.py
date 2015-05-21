#! /usr/bin/python

__author__ = "jeffrey"
__date__ = "$2015/5/21 下午 01:56:41$"

def make_priority_sorter(group):
    """ 該函數返回的is_in_group稱為閉包，make_priority_sorter函數不妨稱為外圍函數，
        is_in_group函數不妨稱為閉包函數。
    
        閉包就是一種數據結構，裡面包含了閉包函數以及環境。此環境會在閉包函數中的每個自由變量
        (free variable，也叫閒置變量，是指定義在閉包函數的外圍作用域中，且在閉包函數裡面用到
        的變量）與該變量名稱在閉包創建時所綁定的值或存儲位置之間建立對應關係。
        
        嚴格來說，閉包是指sorter1 = make_priority_sorter(group1)這種語句中的sorter1，
        而不是泛指is_in_group函數。
        
        在Java等語言裡，外圍函數相當於外部類，閉包函數相當於實現了某接口或某項類的內部類中
        的接口函數（或Java 8中的lambda）。這個內部類的實例，可以設為外部類的實例變量。而外部
        類的其他實例變量，則可以充當閉包中的自由變量。所謂創建閉包，就是創建外部類的實例，然後
        通過該實例的實例變量來調用閉包函數。
    """
    def is_in_group(x):
        if x in group:
            return (0, x)
        else:
            return (1, x)
    
    return is_in_group;

if __name__ == "__main__":
    import os
    
    values = list(os.urandom(10))
    print("Values to sort: " + str(values))
    
    group1 = list(range(100))
    print("The important group A: " + str(group1))
    sorter1 = make_priority_sorter(group1)
    values.sort(key=sorter1)
    print("Sorted values: " + str(values))
    
    group2 = list(range(100, 200))
    print("The important group B: " + str(group2))
    sorter2 = make_priority_sorter(group2)
    values.sort(key=sorter2)
    print("Sorted values: " + str(values))