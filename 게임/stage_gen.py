
from pico2d import *
import gfw
import enemy
import json

enemies = []
time = 0
index = 0

class DictObj:
    def __init__(self, dict):
        self.__dict__.update(dict)

def init():
    global enemies, time, index
    with open('res/stage_02.json') as f:
        data = json.load(f)
        enemies = list(map(DictObj, data))
    time = 0
    index = 0

def update():
    global index

    if index >= len(enemies):
        return

    # if gfw.world.count_at(gfw.layer.player) == 0:
    #     return

    global time
    time += gfw.delta_time
    o = enemies[index]
    # print(time, o.time)
    if time < o.time:
        return

    obj = enemy.enemy_Nomal(
        o.image, o.Mfidx, o.Mfidy,
        o.image_destroy, o.d_Mfidx, o.d_Mfidy,
        o.last_line_image_count, #'enemy01_bomb.png', 5, 5, 1, 
        o.start_x, o.start_y, o.dst_x, o.dst_y, #x // 100 * n, y, 0, 0,
        o.bullet_image, o.shooting_pattern, o.moving_pattern,
        o.speed, o.bullet_speed, o.hp, o.MOVE_PPS)#'enemy01_bullet.png', 4, 0, 100, 3, 10)
    gfw.world.add(gfw.layer.enemy, obj)

    index += 1

def draw():
    pass

def load(file):
    pass