from MyLibrary import *
import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("12")
timer = pygame.time.Clock()

player_group = pygame.sprite.Group()
player = MySprite()
player.load("farmer walk.png", 96, 96, 8)
player.position = 80, 80
player_group.add(player)

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if  event.type == QUIT:
            sys.exit()
            
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
            
    screen.fill((50, 50, 100))
    player_group.update(ticks, 50)
    player_group.draw(screen)
    
    pygame.display.update()