# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="jeffrey"
__date__ ="$2014/7/11 上午 12:13:06$"

if __name__ == "__main__":
    print("Hello World")
    print("hi world!")
from math import *
from TurtleWorld import * 
world = TurtleWorld.TurtleWorld()
t=TurtleWorld.Turtle(world)
def aa(x):
	b = float(x/3)
	t.fd(b)
	t.lt(60)
	t.fd(b)
	t.lt(240)
	t.fd(b)
	t.lt(60)
	t.fd(b)
def bb(x,n):
	if n>0:
		aa(x)
		t.lt(60)
		bb(x,n-1)
		aa(x)
		t.lt(240)
                aa(x)
                t.lt(60)
                aa(x)
                bb(x,n-1)  
                aa(x)
                t.lt(60)
                aa(x)
                t.lt(240)
		aa(x)
                t.lt(60)
		bb(x,n-1)		
		aa(x)
	else:
		t.lt(360)    
    

