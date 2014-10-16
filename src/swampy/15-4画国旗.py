import World

class Canvas:
    def __init__(self):
        self.canvas=world.ca(width=500,height=500,background='white')

class Rectangle:
    def __init__(self):
        self.bbox=[[-150,-100],[150,100]]

def draw_rectangle(my_canvas,rect):
    my_canvas.canvas.rectangle(rect.bbox,outline="black",width=2,fill="green4")

world=World.World()
canvas=Canvas()
rectangle=Rectangle()
draw_rectangle(canvas,rectangle)
world.wait_for_user()