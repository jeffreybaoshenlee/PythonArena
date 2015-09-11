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
        
    def __str__(self):
        return "(X: " + "{:.0f}".format(self.__x) + \
            ",Y: " + " {: .0f}".format(self.__y) + ")"
                
def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

def wrap_angle(angle):
    return angle % 360

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")
font = pygame.font.Font(None, 18)

space = pygame.image.load("space.png").convert_alpha()
planet = pygame.image.load("planet2.png").convert_alpha()
ship = pygame.image.load("freelance.png").convert_alpha()
width, height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (width // 2, height // 2))

radius = 250
angle = 90
pos = Point(0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
        
    screen.blit(space, (0, 0))
    
    angle = wrap_angle(angle-1)
    pos.x = math.cos(math.radians(angle)) * radius
    pos.y = math.sin(math.radians(angle)) * radius

    rotate_angle = -wrap_angle(angle-120)
    scratch_ship = pygame.transform.rotate(ship, rotate_angle)
    
    width, height = scratch_ship.get_size()
    x = 400 + pos.x-width // 2
    y = 300 + pos.y -height // 2
    screen.blit(scratch_ship, (x, y))
    
    print_text(font, 0, 0, "Orbit: " + "{:.0f}".format(angle))
    print_text(font, 0, 40, "Position: " + str(pos))
    
    pygame.display.update()