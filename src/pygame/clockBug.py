__author__ = "huiqiangfov"
__date__ = "$2015-6-4 1:41:16$"

import datetime
import math
import pygame
from pygame.locals import *
import random
import sys

TITLE = "angle clock demo"
FONT_SIZE = 36

HORIZONTAL_RES = 600
VERTICAL_RES = 500

FULL_CIRCLE_ANGLE = 360

HOUR_PER_HALF_DAY = 12
DEGREE_PER_HOUR = FULL_CIRCLE_ANGLE / HOUR_PER_HALF_DAY
MINUTE_PER_HOUR = 60
DEGREE_PER_MINUTE = FULL_CIRCLE_ANGLE / MINUTE_PER_HOUR
SECOND_PER_MINUTE = 60
DEGREE_PER_SECOND = FULL_CIRCLE_ANGLE / SECOND_PER_MINUTE

def set_display():
    resolution = (HORIZONTAL_RES, VERTICAL_RES)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption(TITLE)
    return screen

def handle_exit():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
                
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

BORDER_RADIUS = VERTICAL_RES / 2
TEXT_RADIUS = BORDER_RADIUS - 20
TEXT_TO_DRAW_POS_OFFSET = -10

CENTER_X = HORIZONTAL_RES // 2
CENTER_Y = VERTICAL_RES // 2
CENTER = CENTER_X, CENTER_Y

HAND_START_DEGREE = -90

def hour_degree(hour):
    return hand_degree(hour, DEGREE_PER_HOUR)

def minute_degree(minute):
    return hand_degree(minute, DEGREE_PER_MINUTE)

def second_degree(second):
    return hand_degree(second, DEGREE_PER_SECOND)

def hand_degree(unit_count, degree_per_unit):
    return unit_count * degree_per_unit + HAND_START_DEGREE

def draw_clock_face():
    for hour in range(1, HOUR_PER_HALF_DAY + 1):
        text_angle = math.radians(hour_degree(hour))
        
        text_to_center_x_offset = math.cos(text_angle) * TEXT_RADIUS
        text_x = CENTER_X + text_to_center_x_offset + TEXT_TO_DRAW_POS_OFFSET
        
        text_to_center_y_offset = math.sin(text_angle) * TEXT_RADIUS
        text_y = CENTER_Y + text_to_center_y_offset + TEXT_TO_DRAW_POS_OFFSET
        
        print_text(text_x, text_y, str(hour))

WHITE = 255, 255, 255

def print_text(x, y, text, color=WHITE):
    text_img = font.render(text, True, color)
    screen.blit(text_img, (x, y))

def draw_hand(degree, radius, color, width):
    radians = math.radians(degree)
    hand_to_center_x_offset = math.cos(radians) * radius
    hand_x = hand_to_center_x_offset + CENTER_X
    hand_to_center_y_offset = math.sin(radians) * radius
    hand_y = hand_to_center_y_offset + CENTER_Y
    hand_pos = (hand_x, hand_y)
    pygame.draw.line(screen, color, CENTER, hand_pos, width)

BACKGROUND_COLOR = (0, 0, 100)

ORANGE = 220, 180, 0
YELLOW = 255, 255, 0
PINK = 255, 100, 100

HOUR_RADIUS = BORDER_RADIUS - 80
HOUR_HAND_COLOR = PINK
HOUR_HAND_WIDTH = 25

MINUTE_RADIUS = BORDER_RADIUS - 60
MINUTE_HAND_COLOR = ORANGE
MINUTE_HAND_WIDTH = 12

SECOND_RADIUS = BORDER_RADIUS - 40
SECOND_HAND_COLOR = YELLOW
SECOND_HAND_WIDTH = 6

BORDER_HALF_WIDTH = 10
BORDER_SMALL_CIRCLE_WIDTH = 6

current_draw_degree = FULL_CIRCLE_ANGLE
border_color = BACKGROUND_COLOR
last_border_color = None

def draw_border(draw_degree, color):
    draw_pos_to_center_x_offset = math.cos(math.radians(draw_degree)) * BORDER_RADIUS
    draw_pos_x = int (CENTER_X + draw_pos_to_center_x_offset)
    draw_pos_to_center_y_offset = math.sin(math.radians(draw_degree)) * BORDER_RADIUS
    draw_pos_y = int (CENTER_Y + draw_pos_to_center_y_offset)
    draw_pos = draw_pos_x, draw_pos_y
    pygame.draw.circle(screen, color, draw_pos, BORDER_HALF_WIDTH, BORDER_SMALL_CIRCLE_WIDTH)

def advance_draw_degree():
    global current_draw_degree
    current_draw_degree += 1
    
    if current_draw_degree >= FULL_CIRCLE_ANGLE:
        current_draw_degree = 0

        global last_border_color
        global border_color
        last_border_color = border_color
        border_color = pick_random_color()

def pick_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)

PIVOT_COLOR = WHITE
PIVOT_RADIUS = 20

pygame.init()
screen = set_display()
font = pygame.font.Font(None, FONT_SIZE)

while True:
    handle_exit()

    screen.fill(BACKGROUND_COLOR)
    draw_clock_face()

    current_time = datetime.datetime.now()
    
    hours = current_time.hour % HOUR_PER_HALF_DAY
    draw_hand(hour_degree(hours), HOUR_RADIUS, HOUR_HAND_COLOR, HOUR_HAND_WIDTH)

    minutes = current_time.minute
    draw_hand(minute_degree(minutes), MINUTE_RADIUS, MINUTE_HAND_COLOR, MINUTE_HAND_WIDTH)
    
    seconds = current_time.second
    draw_hand(second_degree(seconds), SECOND_RADIUS, SECOND_HAND_COLOR, SECOND_HAND_WIDTH)
    
    advance_draw_degree()
    for degree in range(0, current_draw_degree):
        draw_border(degree, border_color)
    for degree in range(current_draw_degree, FULL_CIRCLE_ANGLE):
        draw_border(degree, last_border_color)

    pygame.draw.circle(screen, PIVOT_COLOR, CENTER, PIVOT_RADIUS)
    
    print_text(0, 0, str(hours) + ":" + str(minutes) + ":" + str(seconds))

    pygame.display.update()