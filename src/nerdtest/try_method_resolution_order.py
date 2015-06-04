#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "jeffrey"
__date__ = "$2015/6/4 下午 03:03:43$"

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(B):
    pass

class F(E,B):
    pass

class G(D,F,C):
    pass

if __name__ == "__main__":
    print(G.mro());

    import pprint
    pprint.pprint(G.mro())