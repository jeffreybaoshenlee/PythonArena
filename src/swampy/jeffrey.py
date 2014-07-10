import TurtleWorld
import math

world = TurtleWorld.TurtleWorld()
turtle = TurtleWorld.Turtle(world)
turtle.set_delay(0.2)

def polygon(n,sideLength,t):
    externalAngle = 360/n

    for i in range(1,n+1):
        t.fd(sideLength)
        t.rt(externalAngle)

def polygonWithLine(n,sideLength,t):
    externalAngle = 360/n

    halfSideLength = sideLength/2.0
    halfInnerAngle = 90-360/(n*2.0)
    halfInnerAngleInRadians= halfInnerAngle*math.pi/180
    lineLength = halfSideLength / math.cos(halfInnerAngleInRadians)
    print(halfInnerAngleInRadians)

    for i in range(1,n+1):
        t.rt(halfInnerAngle)
        t.fd(lineLength)
        t.rt(180)
        t.pu()
        t.fd(lineLength)
        t.rt(180-halfInnerAngle)
        t.pd()
        t.fd(sideLength)
        t.rt(externalAngle)

def circle(radius,t):
    sideLength = radius * 2 * math.pi / 360
    polygon(360,sideLength,t)

def clear():
    world.clear()
