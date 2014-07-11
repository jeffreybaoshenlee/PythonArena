import math
import TurtleWorld
world = TurtleWorld.TurtleWorld()
t = TurtleWorld.Turtle(world)
t.delay = 0.02
def aa(x):
	a = float(x)
	t.fd(a/3)
	t.lt(60)
	t.fd(a/3)
	t.lt(240)
	t.fd(a/3)
	t.lt(60)
	t.fd(a/3)
def bb(x):
	aa(x)
	t.lt(60)
	aa(x)
	t.lt(240)
	aa(x)
	t.lt(60)
	aa(x)
def dd(x):
	bb(x)
	t.lt(60)
	bb(x)
	t.lt(240)
	bb(x)
	t.lt(60)
	bb(x)	
def ff(n,x):
	for i in range(n):
		dd(x)
		t.lt(60)
		dd(x)
		t.lt(240)
		dd(x)
		t.lt(60)
		dd(x)
def gg(n,x):
	ff(n,x)
	t.lt(240)
	ff(n,x)
	t.lt(240)
	ff(n,x)
gg(1,15)	
	
