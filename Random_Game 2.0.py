import pygame as pg
from random import *
from math import degrees, atan2

pg.init()

# [0] forward
# [1] down
# [2] back
# [3] up

screen_dimension = (2500, 1385)
# screen_dimension = (2500, 500)
screen = pg.display.set_mode(screen_dimension, pg.RESIZABLE)
pg.display.set_caption("PLS HELP ME")

BACKRGOUND_COLOR = (15, 40, 60)
SIDE_PANEL_COLOR = (75, 75, 75)
HEALTH_COLOR = (230, 70, 70)
SIDE_PANEL_BACKGROUND_COLOR = (0, 0, 0)

laser_list = []
LASER_SIZE = (20, 6)
LASER_COOLDOWN = 5

THROTTLE_CHANGE_RATE = 5

time_since_laser = LASER_COOLDOWN

SIDE_PANEL_PADDING = screen_dimension[0]/40
SIDE_PANEL_LENGTH = screen_dimension[0]/5

THROTTLE_COLOR = (0, 0, 0)

LASER_COOLDOWN = 1
time_since_laser = 1000

class Player:
    def __init__(self, momentum, rotation, health, is_alive, acceleration_speed, deceleration_speed, turn_speed, max_speed_modifier, size, pos, throttle, laser_speed, laser_range, laser_damage):
        self.momentum = momentum
        self.rotation = rotation
        self.health = health
        self.is_alive = is_alive
        self.acceleration_speed = acceleration_speed
        self.max_speed_modifier = max_speed_modifier
        self.deceleration_speed = deceleration_speed
        self.turn_speed = turn_speed
        self.size = size
        self.pos = pos
        self.throttle = throttle
        self.max_speed = (self.throttle/7) * self.max_speed_modifier
        self.laser_speed = laser_speed
        self.laser_range = laser_range
        self.laser_damage = laser_damage

    def update_player(self, player):
        if player.is_player_alive():
            player.momentum = self.calc_momentum(player.rotation)
            # print("momentum: ", self.momentum)
            player.pos[0] += player.momentum[0]
            player.pos[1] += player.momentum[1]
            player.pos[0] -= player.momentum[2]
            player.pos[1] -= player.momentum[3]

            if player.did_player_hit_wall():
                player.on_wall_hit()
        else:
            player.is_alive = False


    def calc_momentum(self, rotation):
        new_rotation = rotation - 90
        if new_rotation < 0:
            new_rotation += 360
        if new_rotation >= 0 and new_rotation < 90:
            self.momentum[0] += self.acceleration_speed * (1 - ((new_rotation - 0) / 90))
            self.momentum[1] += self.acceleration_speed * ((new_rotation - 0) / 90)
            self.momentum[2] -= self.deceleration_speed * (1 - ((new_rotation - 0) / 90))
            self.momentum[3] -= self.deceleration_speed * ((new_rotation - 0) / 90)

        elif new_rotation >= 90 and new_rotation < 180:
            self.momentum[1] += self.acceleration_speed * (1 - ((new_rotation - 90) / 90))
            self.momentum[2] += self.acceleration_speed * ((new_rotation - 90) / 90)
            self.momentum[3] -= self.deceleration_speed * (1 - ((new_rotation - 90) / 90))
            self.momentum[0] -= self.deceleration_speed * ((new_rotation - 90) / 90)

        elif new_rotation >= 180 and new_rotation < 270:
            self.momentum[2] += self.acceleration_speed * (1 - ((new_rotation - 180) / 90))
            self.momentum[3] += self.acceleration_speed * ((new_rotation - 180) / 90)
            self.momentum[0] -= self.deceleration_speed * (1 - ((new_rotation - 180) / 90))
            self.momentum[1] -= self.deceleration_speed * ((new_rotation - 180) / 90)

        elif new_rotation >= 270 and new_rotation < 360:
            self.momentum[3] += self.acceleration_speed * (1 - ((new_rotation - 270) / 90))
            self.momentum[0] += self.acceleration_speed * (new_rotation / 90)
            self.momentum[1] -= self.deceleration_speed * (1 - ((new_rotation - 270) / 90))
            self.momentum[2] -= self.deceleration_speed * ((new_rotation - 270) / 90)

        else:
            print("I don't know which way to go!: ", new_rotation)

        for i in range(len(self.momentum)):
            if self.momentum[i] > self.max_speed:
                self.momentum[i] = self.max_speed
            if self.momentum[i] < 0:
                self.momentum[i] = 0

        return self.momentum

    def did_player_hit_wall(self):
        # if self.pos[0] >= screen_dimension[0] - self.size[0] or self.pos[0] <= 0 + SIDE_PANEL_LENGTH or self.pos[1] >= screen_dimension[1] - self.size[1] or self.pos[1]:
        #     return True
        # else:
        #     return False
        return False

    def on_wall_hit(self):
        return False
        # if self.is_alive:
            # wall = self.which_wall_hit()
            # if wall == 0 or wall == 1:
            #     self.health -= abs(self.momentum[0] - self.momentum[2])*10
            #     x = self.momentum[0]
            #     self.momentum[0] = self.momentum[2]
            #     self.momentum[2] = x
            # else:
            #     self.health -= abs(self.momentum[1] - self.momentum[3])*10
            #     x = self.momentum[1]
            #     self.momentum[1] = self.momentum[3]
            #     self.momentum[3] = x

            # if self.health < 0:
            #     self.health = 0

    def which_wall_hit(self):
        if self.pos[0] < SIDE_PANEL_LENGTH:
            return 0
        elif self.pos[0] >= screen_dimension[0] - self.size[0]:
            return 1
        elif self.pos[1] + self.size[1] <= 0:
            return 2
        else:
            return 3

    def is_player_alive(self):
        if self.health > 0:
            return True
        return False

class Laser:
    def __init__(self, pos, rotation, range, speed, damage):
        self.pos = pos
        self.rotation = rotation
        self.range = range
        self.speed = speed
        self.damage = damage

    def update(self, laser):
        if laser.rotation > 360:
            laser.rotation -= 360
        elif laser.rotation < 0:
            laser.rotation += 360

        if laser.rotation >= 0 and laser.rotation < 90:
            laser.pos[0] += laser.speed * (1 - ((laser.rotation - 0) / 90))
            laser.pos[1] += laser.speed * ((laser.rotation - 0) / 90)

        elif laser.rotation >= 90 and laser.rotation < 180:
            laser.pos[1] += laser.speed * (1 - ((laser.rotation - 90) / 90))
            laser.pos[0] -= laser.speed * ((laser.rotation - 90) / 90)

        elif laser.rotation >= 180 and laser.rotation < 270:
            laser.pos[0] -= laser.speed * (1 - ((laser.rotation - 180) / 90))
            laser.pos[1] -= laser.speed * ((laser.rotation - 180) / 90)

        elif laser.rotation >= 270 and laser.rotation < 360:
            laser.pos[1] -= laser.speed * (1 - ((laser.rotation - 270) / 90))
            laser.pos[0] += laser.speed * ((laser.rotation - 270) / 90)

class AI:
    def __init__(self, mode):
        self.mode = mode

    def nav(destination, player):
        change_x = player.pos[0] - destination[0]
        change_y = player.pos[1] - destination[1]
        angle = degrees(atan2(change_y, change_x))
        # print("angle: ", angle)
        # if abs(player.rotation - angle) < abs(360 - angle - player.rotation):
        #     print("clockwise")
        #     return -1 * player.turn_speed
        # elif angle == player.rotation:
        #     print("forward")
        #     return 0
        # else:
        #     print("counter clockwise")
        #     return player.turn_speed
        player.rotation = angle - 90

class Draw:
    def __init__(self, screen_dimension, player_list):
        self.screen_dimension = screen_dimension
        self.player_list = player_list
        self.background = pg.image.load('Random_Game_Images/background.png')
        self.background = pg.transform.scale(self.background, (2000, 2000))
        self.laser_image = pg.image.load('Random_Game_Images/laser.png')
        self.laser_image = pg.transform.scale(self.laser_image, LASER_SIZE)

    def draw_game(self, player, player_list):
        screen.fill(BACKRGOUND_COLOR)
        # background = pg.transform.scale(background, (screen_dimension[0] * 2, screen_dimension[1] * 2))
        angle = -1 * player.rotation
        pivot = (self.screen_dimension[0]/2, self.screen_dimension[1]/2)
        offset = pg.math.Vector2(self.background.get_width() / 2 - player.pos[0], self.background.get_height() / 2 - player.pos[1])
        background_cp = self.background.copy()

        for laser in laser_list:
            laser.update(laser)
            self.draw_laser(laser, background_cp)

        for i in range(1, len(player_list)):
            self.draw_ai(player_list[i], background_cp, i)
   
        rotate = False
        if rotate:
            rotated_image, rect = self.rotate(background_cp, angle, pivot, offset)
            screen.blit(rotated_image, rect)
            self.draw_player(player_list[0])
        else:
            self.draw_ai(player_list[0], background_cp, 0)
            screen.blit(background_cp, background_cp.get_rect(center=pivot))

        self.draw_side_panel(player_list[0])

        pg.display.update()

    def rotate(self, surface, angle, pivot, offset):
        rotated_image = pg.transform.rotozoom(surface, -angle+ 90, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle - 90)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        # print(player.pos, angle, offset, rotated_offset, rect)
        return rotated_image, rect  # Return the rotated image and shifted rect.

    def draw_player(self, player):
        if player.is_alive:
            print("rotation: ", player.rotation, "momentum: ", player.momentum)
            player_1 = pg.image.load('Random_Game_Images/player_1_icon.png')
            player_1 = pg.transform.scale(player_1, player.size)
            # player_1 = pg.transform.rotate(player_1, 90)
            screen.blit(player_1, (screen_dimension[0] / 2 - player.size[0] / 2, screen_dimension[1] / 2 - player.size[1] / 2))
        else:
            player_1 = pg.image.load('Random_Game_Images/explosion.png')
            player_1 = pg.transform.scale(player_1, player.size)
            self.background.blit(player_1, (screen_dimension[0] / 2 - player.size[0] / 2, screen_dimension[1] / 2 - player.size[1] / 2))

    def draw_ai(self, player, surface, number):
        if number == 0:
            player_1 = pg.image.load('Random_Game_Images/player_1_icon.png')
        elif number == 1:
            player_1 = pg.image.load('Random_Game_Images/player_2_icon.png')
        player_1 = pg.transform.scale(player_1, player.size)
        player_1 = pg.transform.rotate(player_1, -1 * player.rotation)
        surface.blit(player_1, player.pos)

    def draw_laser(self, laser, surface):
        rotated_laser_image = pg.transform.rotate(self.laser_image, laser.rotation * -1)
        surface.blit(rotated_laser_image, (laser.pos[0], laser.pos[1]))

    def draw_side_panel(self, player):
        pg.draw.rect(screen, SIDE_PANEL_COLOR, ((0, 0), (SIDE_PANEL_LENGTH, screen_dimension[1])))
        self.draw_player_health(player.health)
        self.draw_player_throttle(player.throttle)

    def draw_player_health(self, health):
        pg.draw.rect(screen, SIDE_PANEL_BACKGROUND_COLOR, ((screen_dimension[0] / 50 - 4, screen_dimension[1] / 25 - 4), (screen_dimension[0]/50 + 8, (screen_dimension[1] * .9) + 8)))
        pg.draw.rect(screen, HEALTH_COLOR, ((screen_dimension[0] / 50, screen_dimension[1] / 25), (screen_dimension[0]/50, screen_dimension[1] * .9)))
        pg.draw.rect(screen, SIDE_PANEL_COLOR, ((screen_dimension[0] / 50, screen_dimension[1] / 25), (screen_dimension[0]/50, (100 - health) * ((screen_dimension[1] * .9) / 100))))

    def draw_player_throttle(self, throttle):
        pg.draw.rect(screen, SIDE_PANEL_BACKGROUND_COLOR, ((screen_dimension[0] / 50 - 4 + SIDE_PANEL_PADDING, screen_dimension[1] / 25 - 4), (screen_dimension[0]/50 + 8, (screen_dimension[1] * .9) + 8)))
        pg.draw.rect(screen, THROTTLE_COLOR, ((screen_dimension[0] / 50 + SIDE_PANEL_PADDING, screen_dimension[1] / 25), (screen_dimension[0]/50, screen_dimension[1] * .9)))
        pg.draw.rect(screen, SIDE_PANEL_COLOR, ((screen_dimension[0] / 50 + SIDE_PANEL_PADDING, screen_dimension[1] / 25), (screen_dimension[0]/50, (100 - throttle) * ((screen_dimension[1] * .9) / 100))))

# player_list = [Player([0, 0, 0, 0], 90, 100, True, 0.2, 0.2, 1, (30, 30), [screen_dimension[0] / 2, screen_dimension[1]/2], 80)]
player_list = [Player(momentum=[0, 10, 0, 0], rotation=0, health=100, is_alive=True, acceleration_speed=0.2, deceleration_speed=0.2, turn_speed=3, max_speed_modifier=1, size=(30, 30), pos=[1000, 1000], throttle=80, laser_speed=20, laser_range = 200, laser_damage=50)]
player_list.append(Player(momentum=[0, 0, 0, 0], rotation=90, health=100, is_alive=True, acceleration_speed=0.1, deceleration_speed=0.2, turn_speed=3, max_speed_modifier=.5, size=(30, 30), pos=[1000, 1000], throttle=80, laser_speed=20, laser_range = 200, laser_damage=50))
draw = Draw(screen_dimension, player_list)

while True:
    pg.time.delay(30)
    for player in player_list:
        player.update_player(player)
    draw.draw_game(player_list[0], player_list)

    for event in pg.event.get():
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_KP_ENTER:
        #         print("restart")
        #         restart()
        if event.type == pg.QUIT:
                pg.quit()
        elif event.type == pg.VIDEORESIZE:
            screen_dimension = pg.display.get_surface().get_size()
            SIDE_PANEL_LENGTH = screen_dimension[0]/5
            draw.draw_game(player_list[0])

    if pg.key.get_pressed()[pg.K_w] and player_list[0].is_alive:
        if player_list[0].throttle < 100:
            player_list[0].throttle += THROTTLE_CHANGE_RATE
            if player_list[0].throttle > 100:
                player_list[0].throttle = 100
            player_list[0].max_speed = (player_list[0].throttle/7) * player_list[0].max_speed_modifier

    if pg.key.get_pressed()[pg.K_s] and player_list[0].is_alive:
        if player_list[0].throttle > 0:  
            player_list[0].throttle -= THROTTLE_CHANGE_RATE
            if player_list[0].throttle < 0:
                player_list[0].throttle = 0
            player_list[0].max_speed = (player_list[0].throttle/7) * player_list[0].max_speed_modifier

    if pg.key.get_pressed()[pg.K_a] and player_list[0].is_alive:
        player_list[0].rotation -= player_list[0].turn_speed
        if player_list[0].rotation < 0:
            player_list[0].rotation += 360

    if pg.key.get_pressed()[pg.K_d] and player_list[0].is_alive:
        player_list[0].rotation += player_list[0].turn_speed
        if player_list[0].rotation >= 360:
            player_list[0].rotation -= 360
            
    if pg.mouse.get_pressed()[0]:
        if time_since_laser >= LASER_COOLDOWN:
            laser_list.append(Laser(player_list[0].pos.copy(), player_list[0].rotation - 90, player_list[0].laser_range, player_list[0].laser_speed, player_list[0].laser_damage))
            # for laser in laser_list:
                # if laser.pos[0] > 2000 or laser.pos[1] > 2000 or laser.pos[0] > 0 or laser.pos[1] > 0:
                #     laser_list.remove(laser)
            time_since_laser = 0

    # player_list[1].rotation += AI.nav(player_list[0].pos, player_list[1])
    AI.nav(player_list[0].pos, player_list[1])
    print(player_list[1].rotation)
    if player_list[1].rotation < 0:
        player_list[1].rotation += 360
    elif player_list[1].rotation >= 360:
        player_list[1].rotation -= 360

    # print(player_list[1].rotation, player_list[1].momentum, player_list[1].pos)

    time_since_laser += 1