from MyLibrary import *
import pygame
from pygame.locals import *
import sys


def calc_velocity(direction, vel=1.0):
    velocity = Point(0,0)
    if direction == 0: #north
        velocity.y = -vel
    elif direction == 2: #east
        velocity.x = vel
    elif direction == 4: #south
        velocity.y = vel
    elif direction == 6: #west
        velocity.x = -vel
    return velocity

def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("12")
timer = pygame.time.Clock()

player_group = pygame.sprite.Group()
player = MySprite()
player.load("farmer walk.png", 96, 96, 8)
player.position = 80, 80
player_group.add(player)

game_over = False
player_moving = False

while True:
    timer.tick(50)
    ticks = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if  event.type == QUIT:
            sys.exit()
            
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        elif keys[K_UP] or keys[K_w]:
            player.direction= 0
            player_moving = True
        elif keys[K_RIGHT] or keys[K_d]:
            player.direction = 2 
            player_moving = True
        elif keys[K_DOWN] or keys[K_s]:
            player.direction = 4
            player_moving = True
        elif keys[K_LEFT] or keys[K_a] :
            player.direction = 6
            player_moving = True
        else:
            player_moving = False
        
        if not game_over:
        #set animation frames based on player's direction
           player.first_frame = player.direction * player.columns
           player.last_frame = player.first_frame + player.columns-1
           if player.frame < player.first_frame:
              player.frame = player.first_frame
           if not player_moving:
            #stop animating when player is not pressing a key
               player.frame = player.first_frame = player.last_frame
           else:
            #move player in direction 
              player.velocity = calc_velocity(player.direction, 1.5)
              player.velocity.x *= 3
              player.velocity.y *= 3
            
    screen.fill((50, 50, 100))
    player_group.update(ticks, 5)
    if player_moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            if player.X < 0: player.X = 0
            elif player.X > 700: player.X = 700
            if player.Y < 0: player.Y = 0
            elif player.Y > 500: player.Y = 500
    
    
    player_group.draw(screen)
    
    pygame.display.update()