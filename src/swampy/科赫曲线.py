import TurtleWorld
import math
world = TurtleWorld.TurtleWorld()
t = TurtleWorld.Turtle(world)
def aa(x):
    b = float(x/3)
    t.fd(b)
def bb(x):
    t.lt(60)
def cc(x):
    t.lt(240)
def dd(x,n):
    if n>0:
        aa(x)
        bb(x)
        aa(x)
        cc(x)
        aa(x)
        bb(x)
        aa(x)
    else:
        t.lt(360)
t.delay = 0.013
def ee(x,n):
    if n>0:
        dd(x,n-2)
        ee(x,n-1)
        dd(x,n-1)
        bb(x)
        dd(x,n-1)
        ee(x,n-1)
        dd(x,n)
        cc(x)
        dd(x,n)
        ee(x,n-1)
        dd(x,n-1)
        bb(x)
        dd(x,n-1)
        ee(x,n-1)
        dd(x,n-2)
    else:
        t.lt(360)
def ff(x,n):
    for i in range(3):
        ee(x,n)
        t.lt(240)
ff(15,4)        