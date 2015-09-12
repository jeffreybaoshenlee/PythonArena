_author__ = "huiqiangfov"
__date__ = "$2015-9-11 1:46:06$"

import math
import pygame
from pygame.locals import *
import sys

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = property(getx, setx)
    
    def gety(self):
        return self.__y
    def sety(self, y):
        self.__y = y
    y = property(gety, sety)
    
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ksjdfj")

class Sourrd(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 0.0
        self.radius = 250.0
        self.pos = Point(0, 0)
        self.old_pos = Point(0, 0)
        self.delta_x = 0.0
        self.delta_y = 0.0
        self.rangle = 0.0
        self.rangled = 0.0
        self.master_image = None
        self.turn_image = None
        self.another = 0
        
    @staticmethod
    def wrap_angle(angle):
        return angle % 360
    
    def turn(self, filename,angle):
        self.master_image = pygame.image.load(filename).convert_alpha()
        
        print("another="+str(self.another))
  
        self.another = self.angle-angle
        self.angle = Sourrd.wrap_angle(self.another)
        print("angle="+str(self.angle))
        self.pos.x = math.sin(math.radians(self.angle)) * self.radius
        self.pos.y = math.cos(math.radians(self.angle)) * self.radius
        self.delta_x = (self.pos.x-self.old_pos.x)
        self.delta_y = (self.pos.y -self.old_pos.y)
        self.rangle = math.atan2(self.delta_y, self.delta_x)
        self.rangled = -self.wrap_angle(math.degrees(self.rangle))
        print(self.rangled)
        self.turn_image = pygame.transform.rotate(self.master_image, self.rangled)
        
        self.old_pos.x = self.pos.x
        self.old_pos.y = self.pos.y
a = Sourrd()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:sys.exit()
    screen.fill((100, 100, 100))
    a.turn("military.png",3)
    width, height = a.turn_image.get_size()
    x = 400 + a.pos.x-width // 2
    y = 300 + a.pos.y -height // 2
    print("x=" + str(x) + ";y=" + str(y))
    screen.blit(a.turn_image, (x, y))
    pygame.display.update()
