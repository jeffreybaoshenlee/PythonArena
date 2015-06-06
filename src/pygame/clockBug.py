__author__ = "huiqiangfov, jeffreybaoshenlee"
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

BACKGROUND_COLOR = (0, 0, 100)

BORDER_RADIUS = VERTICAL_RES / 2
TEXT_RADIUS = BORDER_RADIUS - 20
TEXT_TO_DRAW_POS_OFFSET = -10

CENTER_X = HORIZONTAL_RES // 2
CENTER_Y = VERTICAL_RES // 2
CENTER = CENTER_X, CENTER_Y

def draw_clock_face():
    for hour in range(1, HOUR_PER_HALF_DAY + 1):
        text_angle = math.radians(_hour_degree(hour))
        
        text_to_center_x_offset = math.cos(text_angle) * TEXT_RADIUS
        text_x = CENTER_X + text_to_center_x_offset + TEXT_TO_DRAW_POS_OFFSET
        
        text_to_center_y_offset = math.sin(text_angle) * TEXT_RADIUS
        text_y = CENTER_Y + text_to_center_y_offset + TEXT_TO_DRAW_POS_OFFSET
        
        _draw_text(text_x, text_y, str(hour))

HAND_START_DEGREE = -90

def _hour_degree(hour):
    return _hand_degree(hour, DEGREE_PER_HOUR)

def _minute_degree(minute):
    return _hand_degree(minute, DEGREE_PER_MINUTE)

def _second_degree(second):
    return _hand_degree(second, DEGREE_PER_SECOND)

def _hand_degree(unit_count, degree_per_unit):
    return unit_count * degree_per_unit + HAND_START_DEGREE

WHITE = 255, 255, 255

def get_time():
    current_time = datetime.datetime.now()
    return current_time.hour, current_time.minute, current_time.second

def _draw_text(x, y, text, color=WHITE):
    text_img = font.render(text, True, color)
    screen.blit(text_img, (x, y))

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

def draw_hands(hours, minutes, seconds):
    hours = hours % HOUR_PER_HALF_DAY
    hour_degree = _hour_degree(hours)
    minute_to_hour_ratio = minutes / MINUTE_PER_HOUR
    hour_degree += DEGREE_PER_HOUR * minute_to_hour_ratio
    draw_hand(hour_degree, HOUR_RADIUS, HOUR_HAND_COLOR, HOUR_HAND_WIDTH)
    
    minute_degree = _minute_degree(minutes)
    second_to_minute_ration = seconds / SECOND_PER_MINUTE
    minute_degree += DEGREE_PER_MINUTE * second_to_minute_ration
    draw_hand(minute_degree, MINUTE_RADIUS, MINUTE_HAND_COLOR, MINUTE_HAND_WIDTH)
    
    draw_hand(_second_degree(seconds), SECOND_RADIUS, SECOND_HAND_COLOR, SECOND_HAND_WIDTH)

def draw_hand(degree, radius, color, width):
    radians = math.radians(degree)
    hand_to_center_x_offset = math.cos(radians) * radius
    hand_x = hand_to_center_x_offset + CENTER_X
    hand_to_center_y_offset = math.sin(radians) * radius
    hand_y = hand_to_center_y_offset + CENTER_Y
    hand_pos = (hand_x, hand_y)
    pygame.draw.line(screen, color, CENTER, hand_pos, width)

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

def draw_dynamic_border():
    global current_draw_degree
    current_draw_degree = _advance_draw_degree(current_draw_degree)
    if current_draw_degree == 0:
        global last_border_color, border_color
        last_border_color = border_color
        border_color = _pick_random_color()
        
    for degree in range(0, current_draw_degree):
        draw_border(degree, border_color)
    for degree in range(current_draw_degree, FULL_CIRCLE_ANGLE):
        draw_border(degree, last_border_color)

BORDER_CHANGE_DEGREE_PER_CYCLE = 4

def _advance_draw_degree(current_draw_degree):
    current_draw_degree += BORDER_CHANGE_DEGREE_PER_CYCLE
    
    if current_draw_degree >= FULL_CIRCLE_ANGLE:
        current_draw_degree = 0
    return current_draw_degree

def _pick_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)

PIVOT_COLOR = WHITE
PIVOT_RADIUS = 20

def draw_pivot():
    pygame.draw.circle(screen, PIVOT_COLOR, CENTER, PIVOT_RADIUS)\

def draw_time(hours, minutes, seconds):
    _draw_text(0, 0, str(hours) + ":" + str(minutes) + ":" + str(seconds))
    
pygame.init()
screen = set_display()
font = pygame.font.Font(None, FONT_SIZE)

while True:
    handle_exit()

    screen.fill(BACKGROUND_COLOR)
    
    draw_clock_face()
    hours, minutes, seconds = get_time()
    draw_hands(hours, minutes, seconds)
    draw_dynamic_border()
    draw_pivot()
    draw_time(hours, minutes, seconds)

    pygame.display.update()