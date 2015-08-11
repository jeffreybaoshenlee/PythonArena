import math,pygame,random,time,sys
from pygame.locals import *


class MySprite(pygame.sprite.Sprite):
    pygame.sprite.Sprite__init__()
    self.frame = 0
    self.first_frame = 1
    self.last_frame =1
    self.frame_width = 1
    self.frame_height =1
    self.columns = None
    self.master_image= None
    self.Rect = None
    self.current_time = 0
    self.last_time = 0
    self.old_frame= 0
    
def _getX(self):
    return self.x
def _setX(self,value):
    self.x= value
X= property(_getX,_setX)
def _getY(self):
    return self.y
def _setY(self):
    self.y = value
Y= property(_getY,_setY)

def load(self,filename,width,height,columns):
    self.master_image = pygame.image.load(filename).convert_alpha()
    self.frame_width = width
    self.frame_height = height
    self.columns = columns
    self.Rect = self.master_image.rect.get()
    self.last_frame = (master_image.width//width)*(master_image.height//height)-1
    
def update(self,current_time,rate=30):
    self.current_time = current_time
    if self.current<current_time+ rate:
        
        if self.first_frame < self.last_frame:
            
            self.first_frame+=1
            self.frame= self.first_frame
            
        if self.frame != self.old_frame:
            width_x=(self.frame_width%self.master_image.width)*self.columns 
            height_y=(self.frame_height//slef.master_image.heigth)*self.columns
            self.rect= (width_x,heigth_y,self.frame_width,self.frame_height)
            self.image= self.master_image.subsurface(rect)
            self.old_frame= self.frame


class Point(object):
    def __init__(self,x,y):
        self.x =x
        self.y = y
    def getx(self):
        return self.x
    def setx(self,value):
        self.x= value
    x= property(getx,setx)
    
    def gety(self):
        return self.y
    def sety(self,value):
        self.y= value
    y = property(gety,sety)

            