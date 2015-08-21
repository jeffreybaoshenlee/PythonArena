from MyLibrary import *
import pygame
from pygame.locals import *
import random
import sys
 
pygame.init()

def calc_velocity(direction, vel=1.0):
    velocity = Point(0, 0)
    if direction == 0:
        velocity.y = -vel
    elif direction == 2:
        velocity.x = vel
    elif direction == 4:
        velocity.y = vel
    elif direction == 6:
        velocity.x = -vel
    return velocity

def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
        print(sprite.direction)
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("12")
timer = pygame.time.Clock()

player_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()

game_over = False
player_moving = False

player = MySprite()
player.load("farmer walk.png", 96, 96, 8)
player.position = 80, 80
player.direction = 6
player_group.add(player)

for z in range(0, 10):
    zombie = MySprite()
    zombie.load("zombie walk.png", 96, 96, 8)
    zombie.position = random.randint(0, 500), random.randint(0, 500)
    zombie.direction = random.randint(0, 3) * 2
    zombie_group.add(zombie)

while True:
    timer.tick(50)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        
        elif keys[K_UP] or keys[K_w]:
            player.direction = 0
            player_moving = True
        elif keys[K_RIGHT] or keys[K_d]:
            player.direction = 2
            player_moving = True
        elif keys[K_DOWN] or keys[K_s]:
            player.direction = 4
            player_moving = True
        elif keys[K_LEFT] or keys[K_a]:
            player.direction = 6
            player_moving = True
        else:
            player_moving = False
            
    if game_over == False:
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns-1
        
        if player.frame < player.first_frame:
            player.frame = player.first_frame
            
        if player_moving == False:
            player.frame = player.first_frame = player.last_frame
        
        if player_moving == True:
            player.velocity = calc_velocity(player.direction, 4)
            player.X += player.velocity.x
            player.Y += player.velocity.y 
            
            if player.X > 700:
                player.X = 700
            elif player.X < 0: 
                player.X = 0
            elif player.Y > 500: 
                player.Y = 500
            elif player.Y < 0: 
                player.Y = 0
                
        player_group.update(ticks, 50)
        zombie_group.update(ticks, 50)
        
        for z in zombie_group:
            z.first_frame = z.direction * z.columns
            z.last_frame = z.first_frame + z.columns-1
            if z.frame < z.first_frame:
                z.frame = z.first_frame
            
            z.velocity = calc_velocity (z.direction)
            z.X += z.velocity.x * 6
            z.Y += z.velocity.y * 6
            
            if z.X < 0 or z.X > 700 or z.Y < 0 or z.Y > 500:
                reverse_direction(z)
            
    screen.fill((100, 100, 100))
    
    player_group.draw(screen)
    zombie_group.draw(screen)
    
    pygame.display.update()