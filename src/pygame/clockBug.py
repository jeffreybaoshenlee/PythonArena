# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "huiqiangfov"
__date__ = "$2015-6-4 1:41:16$"
import sys, random,pygame,time,math
from pygame.locals import *

from datetime import datetime,date,time

def print_text(font,x,y,text,color= (255,255,255)):
    imgText= font.render(text,True,color)
    screen.blit(imgText,(x,y))

def wrap_angle(angle):
    return angle %360

pygame.init()
screen= pygame.display.set_mode((600,500))
pygame.display.set_caption("angle clock demo")
font= pygame.font.Font(None,36)

orange= 220,180,0
white = 255,255,255
yellow= 255,255,0
pink= 255,100,100

pos_x = 300
pos_y = 250
radius = 250
angle = 360
angle1=360

while True:
    for event in pygame.event.get():
        if event.type== QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
        
    screen.fill((0,0,100))
    

    
    for n in range(1,13):
        angle = math.radians(n*(360/12)-90)
        x = math.cos(angle)* (radius-20)-10
        y = math.sin(angle)* (radius-20)-10
        print_text(font,pos_x+x,pos_y+y,str(n))
        
    today = datetime.today()
    hours = today.hour%12
   
    minutes = today.minute
    seconds = today.second
    
    hour_angle= wrap_angle(hours*(360/12)-90)
  
    hour_angle= math.radians(hour_angle)
    hour_x = math.cos(hour_angle)*(radius-80)
    hour_y = math.sin(hour_angle)*(radius-80)
    target= (pos_x+hour_x,pos_y+hour_y)
    pygame.draw.line(screen,pink,(pos_x,pos_y),target,25)
    
    
    min_angle= wrap_angle(minutes * (360/60)-90)
    min_angle= math.radians(min_angle)
    min_x = math.cos(min_angle) * (radius-60)
    min_y = math.sin(min_angle) * (radius-60)
    target= (pos_x+min_x,pos_y+min_y)
    pygame.draw.line(screen,orange,(pos_x,pos_y),target,12)
    
    sec_angle= wrap_angle(seconds * (360/60)-90)
    sec_angle= math.radians(sec_angle)
    sec_x= math.cos(sec_angle)* (radius-40)
    sec_y= math.sin(sec_angle)*(radius-40)
    target= (pos_x+sec_x,pos_y+sec_y)
    pygame.draw.line(screen,yellow,(pos_x,pos_y),target,6)
    
    angle1+=1
    if angle1 >=360:
        angle1=0
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        color1=r,g,b
    x1=math.cos(math.radians(angle1))*radius
    y1 =math.sin(math.radians(angle1))*radius
    
    pos1=(int(pos_x+x1),int(pos_y+y1))
   
    pygame.draw.circle(screen,color1,pos1,10,0)
    
    pygame.draw.circle(screen,white,(pos_x,pos_y),20)
    
    print_text(font,0,0,str(hours)+":"+str(minutes)+":"+str(seconds))
    


    pygame.display.update()