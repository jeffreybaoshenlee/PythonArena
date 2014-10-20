import World

class Canvas:
    def __init__(self):
        self.canvas=world.ca(width=500,height=500,background='white')

class Rectangle:
    def __init__(self):
        self.bbox=[[-150,-100],[150,100]]
        self.color='blue'

class Point:
    
    def __init__(self):
        self.points1=[[-150,-100],[-50,0],[150,0],[150,-100]]
        self.color1='red'
        self.points2=[[-150,100],[-50,0],[150,0],[150,100]]
        self.color2='white'

def draw_rectangle(a,b):
    a.canvas.rectangle(b.bbox,outline="black",width=2,fill=b.color)



def draw_polygon(a,b):
    a.canvas.polygon(b.points1,fill=b.color1)
    a.canvas.polygon(b.points2,fill=b.color2)
    

world=World.World()
canvas=Canvas()
rectangle=Rectangle()

point=Point()
draw_rectangle(canvas,rectangle)

draw_polygon(canvas,point)
world.wait_for_user()