# Copyright 2020 Damian Piech
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pygame as pg
from random import *

pg.init()

# [0] forward
# [1] down
# [2] back
# [3] up

screen_dimension = (2500, 1385)
# screen_dimension = (2500, 500)
screen = pg.display.set_mode(screen_dimension, pg.RESIZABLE)
player_1_momentum = [0, 0, 0, 0]
player_1_rotation = 0
player_1_is_alive = True
player_1_health = 100

player_1_throttle = 80

max_speed = player_1_throttle/7
acceleration_speed = max_speed/90
DECELERATION_SPEED = .2  
SIDE_PANEL_LENGTH = screen_dimension[0]/5

PLAYER_SIZE = (65, 65)

player_1_pos = [50 + SIDE_PANEL_LENGTH, screen_dimension[1] / 2]

BACKRGOUND_COLOR = (15, 40, 60)
SIDE_PANEL_COLOR = (75, 75, 75)
HEALTH_COLOR = (230, 70, 70)
SIDE_PANEL_BACKGROUND_COLOR = (0, 0, 0)

laser_list = []
LASER_SPEED = 10
LASER_SIZE = (20, 6)
LASER_COOLDOWN = 5

THROTTLE_CHANGE_RATE = .5
TURN_SPEED = 3

time_since_laser = LASER_COOLDOWN

SIDE_PANEL_PADDING = screen_dimension[0]/40


THROTTLE_COLOR = (0, 0, 0)

def draw_game():
    screen.fill(BACKRGOUND_COLOR)
    draw_player_1()
    draw_side_panel()
    draw_lasers()
    pg.display.update()

def draw_player_1():
    global player_1_rotation
    if player_1_is_alive:
        player_1 = pg.image.load('Random_Game_Images/player_1_icon.png')
        player_1 = pg.transform.scale(player_1, PLAYER_SIZE)
        player_1 = pg.transform.rotate(player_1, player_1_rotation * -1)
        screen.blit(player_1, player_1_pos)
    else:
        player_1 = pg.image.load('Random_Game_Images/explosion.png')
        player_1 = pg.transform.scale(player_1, PLAYER_SIZE)
        screen.blit(player_1, player_1_pos)

def draw_side_panel():
    pg.draw.rect(screen, SIDE_PANEL_COLOR, ((0, 0), (SIDE_PANEL_LENGTH, screen_dimension[1])))
    draw_player_1_health(player_1_health)
    draw_player_1_throttle(player_1_throttle)

def draw_player_1_health(health):
    pg.draw.rect(screen, SIDE_PANEL_BACKGROUND_COLOR, ((screen_dimension[0] / 50 - 4, screen_dimension[1] / 25 - 4), (screen_dimension[0]/50 + 8, (screen_dimension[1] * .9) + 8)))
    pg.draw.rect(screen, HEALTH_COLOR, ((screen_dimension[0] / 50, screen_dimension[1] / 25), (screen_dimension[0]/50, screen_dimension[1] * .9)))
    pg.draw.rect(screen, SIDE_PANEL_COLOR, ((screen_dimension[0] / 50, screen_dimension[1] / 25), (screen_dimension[0]/50, (100 - health) * ((screen_dimension[1] * .9) / 100))))

def draw_player_1_throttle(throttle):
    pg.draw.rect(screen, SIDE_PANEL_BACKGROUND_COLOR, ((screen_dimension[0] / 50 - 4 + SIDE_PANEL_PADDING, screen_dimension[1] / 25 - 4), (screen_dimension[0]/50 + 8, (screen_dimension[1] * .9) + 8)))
    pg.draw.rect(screen, THROTTLE_COLOR, ((screen_dimension[0] / 50 + SIDE_PANEL_PADDING, screen_dimension[1] / 25), (screen_dimension[0]/50, screen_dimension[1] * .9)))
    pg.draw.rect(screen, SIDE_PANEL_COLOR, ((screen_dimension[0] / 50 + SIDE_PANEL_PADDING, screen_dimension[1] / 25), (screen_dimension[0]/50, (100 - throttle) * ((screen_dimension[1] * .9) / 100))))

def restart():
    global player_1_momentum
    global player_1_rotation
    global player_1_is_alive
    global max_speed
    global acceleration_speed
    global player_1_pos
    global player_1_health
    global player_1_throttle

    player_1_momentum = [0, 0, 0, 0]
    player_1_rotation = 0
    player_1_is_alive = True
    player_1_health = 100

    player_1_throttle = 80

    max_speed = player_1_throttle/7
    acceleration_speed = max_speed/90

    player_1_pos = [50 + SIDE_PANEL_LENGTH, screen_dimension[1] / 2]

def calc_momentum():
    if player_1_rotation >= 0 and player_1_rotation < 90:
        # print("0 - 90")
        player_1_momentum[0] += acceleration_speed * (1 - ((player_1_rotation - 0) / 90))
        player_1_momentum[1] += acceleration_speed * ((player_1_rotation - 0) / 90)
        player_1_momentum[2] -= DECELERATION_SPEED * (1 - ((player_1_rotation - 0) / 90))
        player_1_momentum[3] -= DECELERATION_SPEED * ((player_1_rotation - 0) / 90)
        # print("0 increased by: {:2} 1 increased by {:2}".format(acceleration_speed * (1 - (player_1_rotation / 90)), acceleration_speed * (player_1_rotation / 90)))

    elif player_1_rotation >= 90 and player_1_rotation < 180:
        # print("90 - 180")
        player_1_momentum[1] += acceleration_speed * (1 - ((player_1_rotation - 90) / 90))
        player_1_momentum[2] += acceleration_speed * ((player_1_rotation - 90) / 90)
        player_1_momentum[3] -= DECELERATION_SPEED * (1 - ((player_1_rotation - 90) / 90))
        player_1_momentum[0] -= DECELERATION_SPEED * ((player_1_rotation - 90) / 90)
        # print("1 increased by: {:17} 2 increased by {:34}".format(acceleration_speed * (1 - (player_1_rotation / 90)), acceleration_speed * (player_1_rotation / 90)))

    elif player_1_rotation >= 180 and player_1_rotation < 270:
        # print("180 - 270")
        player_1_momentum[2] += acceleration_speed * (1 - ((player_1_rotation - 180) / 90))
        player_1_momentum[3] += acceleration_speed * ((player_1_rotation - 180) / 90)
        player_1_momentum[0] -= DECELERATION_SPEED * (1 - ((player_1_rotation - 180) / 90))
        player_1_momentum[1] -= DECELERATION_SPEED * ((player_1_rotation - 180) / 90)
        # print("2 increased by: {:17} 3 increased by {:34}".format(acceleration_speed * (1 - (player_1_rotation / 90)), acceleration_speed * (player_1_rotation / 90)))

    elif player_1_rotation >= 270 and player_1_rotation < 360:
        # print("270 - 360")
        player_1_momentum[3] += acceleration_speed * (1 - ((player_1_rotation - 270) / 90))
        player_1_momentum[0] += acceleration_speed * (player_1_rotation / 90)
        player_1_momentum[1] -= DECELERATION_SPEED * (1 - ((player_1_rotation - 270) / 90))
        player_1_momentum[2] -= DECELERATION_SPEED * ((player_1_rotation - 270) / 90)
        # print("3 increased by: {:17} 0 increased by {:34}".format(acceleration_speed * (1 - ((player_1_rotation / 90)), acceleration_speed * (player_1_rotation / 90)))

    else:
        print("error: ", player_1_rotation)

    for i in range(len(player_1_momentum)):
        if player_1_momentum[i] > max_speed:
            player_1_momentum[i] = max_speed
        if player_1_momentum[i] < 0:
            player_1_momentum[i] = 0

        print(player_1_momentum)
    return player_1_momentum

def which_wall_hit():
    if player_1_pos[0] < SIDE_PANEL_LENGTH:
        return 0
        # Left Wall
    elif player_1_pos[0] >= screen_dimension[0] - PLAYER_SIZE[0]:
        return 1
        # Right Wall
    elif player_1_pos[1] + PLAYER_SIZE[1] <= 0:
        return 2
        # Bottom Wall
    else:
        return 3
        # Top Wall

def on_wall_hit():
    global momentum
    global player_1_health
    global player_1_rotation
    if player_1_is_alive:
        wall = which_wall_hit()
        if wall == 0 or wall == 1:
            player_1_health -= abs(player_1_momentum[0] - player_1_momentum[2])*10
            x = player_1_momentum[0]
            player_1_momentum[0] = player_1_momentum[2]
            player_1_momentum[2] = x
        else:
            player_1_health -= abs(player_1_momentum[1] - player_1_momentum[3])*10
            x = player_1_momentum[1]
            player_1_momentum[1] = player_1_momentum[3]
            player_1_momentum[3] = x

        if player_1_health < 0:
            player_1_health = 0

def did_player_hit_wall(self):
    if self.pos(0) >= screen_dimension[0] - PLAYER_SIZE[0] or self.pos(0) <= 0 + SIDE_PANEL_LENGTH or self.pos(1) >= screen_dimension[1] - PLAYER_SIZE[1] or self.pos(1):
        return True
    else:
        return False

# def did_laser_hit_player(player_pos_x, player_pos_y,)
#     if pos_x >= screen_dimension[0] - PLAYER_SIZE[0] or pos_x <= 0 + SIDE_PANEL_LENGTH or pos_y >= screen_dimension[1] - PLAYER_SIZE[1] or pos_y <= 0:
#         return True
#     else:
#         return False

def player_fire_laser(fire_pos_x, fire_pos_y, direction):
    global laser_list
    offset = (10, 10)
    laser_list.append([fire_pos_x + offset[0], fire_pos_y + offset[1], direction])

def update_lasers():
    for i in range(len(laser_list)):
        if laser_list[i][2] >= 0 and laser_list[i][2] < 90:
            laser_list[i][0] += LASER_SPEED * (1 - ((laser_list[i][2] - 0) / 90))
            laser_list[i][1] += LASER_SPEED * ((laser_list[i][2] - 0) / 90)

        elif laser_list[i][2] >= 90 and laser_list[i][2] < 180:
            laser_list[i][1] += LASER_SPEED * (1 - ((laser_list[i][2] - 90) / 90))
            laser_list[i][0] -= LASER_SPEED * ((laser_list[i][2] - 90) / 90)

        elif laser_list[i][2] >= 180 and laser_list[i][2] < 270:
            laser_list[i][0] -= LASER_SPEED * (1 - ((laser_list[i][2] - 180) / 90))
            laser_list[i][1] -= LASER_SPEED * ((laser_list[i][2] - 180) / 90)

        elif laser_list[i][2] >= 270 and laser_list[i][2] < 360:
            laser_list[i][1] -= LASER_SPEED * (1 - ((laser_list[i][2] - 270) / 90))
            laser_list[i][0] += LASER_SPEED * ((laser_list[i][2] - 270) / 90)
        
        if laser_list[i][0] >= screen_dimension[0] - LASER_SIZE[0] or laser_list[i][0] <= 0 + SIDE_PANEL_LENGTH or laser_list[i][1] >= screen_dimension[1] - LASER_SIZE[1] or laser_list[i][1] <= 0:
            del(laser_list[i])
            break

def draw_lasers():
    for laser in laser_list:
        laser_image = pg.image.load('Random_Game_Images/laser.png')
        laser_image = pg.transform.scale(laser_image, LASER_SIZE)
        laser_image = pg.transform.rotate(laser_image, laser[2] * -1)
        screen.blit(laser_image, (laser[0], laser[1]))

draw_game()

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_KP_ENTER:
                print("restart")
                restart()
        elif event.type == pg.QUIT:
                pg.quit()
        elif event.type == pg.VIDEORESIZE:
            screen_dimension = pg.display.get_surface().get_size()
            SIDE_PANEL_LENGTH = screen_dimension[0]/5
            draw_game()

    if pg.key.get_pressed()[pg.K_a] and player_1_is_alive:
        player_1_rotation -= TURN_SPEED
        if player_1_rotation < 0:
            player_1_rotation += 360

    if pg.key.get_pressed()[pg.K_d] and player_1_is_alive:
        player_1_rotation += TURN_SPEED
        if player_1_rotation >= 360:
            player_1_rotation -= 360

    if pg.mouse.get_pressed()[0]:
        if time_since_laser == LASER_COOLDOWN:
            player_fire_laser(player_1_pos[0] + PLAYER_SIZE[0]/2, player_1_pos[1] + PLAYER_SIZE[1]/2, player_1_rotation)
            time_since_laser = 0

    if pg.key.get_pressed()[pg.K_w] and player_1_is_alive:
        if player_1_throttle < 100:
            player_1_throttle += THROTTLE_CHANGE_RATE
            if player_1_throttle > 100:
                player_1_throttle = 100
            max_speed = player_1_throttle/7
            acceleration_speed = max_speed/90

    if pg.key.get_pressed()[pg.K_s] and player_1_is_alive:
        if player_1_throttle > 0:  
            player_1_throttle -= THROTTLE_CHANGE_RATE
            if player_1_throttle < 0:
                player_1_throttle = 0
            max_speed = player_1_throttle/7
            acceleration_speed = max_speed/90

    update_lasers()

    if player_1_is_alive:
        player_1_momentum = calc_momentum()

        player_1_pos[0] += player_1_momentum[0]
        player_1_pos[1] += player_1_momentum[1]
        player_1_pos[0] -= player_1_momentum[2]
        player_1_pos[1] -= player_1_momentum[3]

    if did_player_hit_wall():
        on_wall_hit()

    # print("rotation: ", player_1_rotation)
    # print("momentum: ", player_1_momentum)
    # print("pos: ", player_1_pos)

    if player_1_health <= 0:
        player_1_is_alive = False

    if time_since_laser < LASER_COOLDOWN:
        time_since_laser += 1

    draw_game()

    pg.time.delay(30)