#! /usr/bin/python

import char_tool

__author__ = "jeffrey"
__date__ = "$2015/5/12 12:57:05$"

if __name__ == "__main__":
    my_str="hello"
    print(my_str)
    
    my_bytes=char_tool.to_bytes(my_str)
    print(my_bytes)
    
    print(my_str==my_bytes)
    print(""==char_tool.to_bytes(""))