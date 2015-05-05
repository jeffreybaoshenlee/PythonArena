# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "huiqiangfov"
__date__ = "$2015-5-5 23:53:47$"

import pygame,time
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
white=255,255,255
blue = 0,0,255
textImage= myfont.render("Hello Pygame",True,white)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
                sys.exit()
    screen.fill(blue)
    screen.blit(textImage,(100,100))
    pygame.display.update()