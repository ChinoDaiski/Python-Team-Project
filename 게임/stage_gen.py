
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
    with open('res/stage_01.json') as f:
        data = json.load(f)
        enemies = list(map(DictObj, data))
    time = 0
    index = 0

def update():
    global index

    if index >= len(enemies):
        return

    global time
    time += gfw.delta_time
    o = enemies[index]
    # print(time, o.time)
    if time < o.time:
        return

    # print(o)
    obj = enemy.enemy_Nomal(
        o.image, o.Mfidx, o.Mfidy,
        o.image_destroy, o.d_Mfidx, o.d_Mfidy,
        o.last_line_image_count, #'enemy01_bomb.png', 5, 5, 1, 
        o.start_x, o.start_y, o.dst_x, o.dst_y, #x // 100 * n, y, 0, 0,
        o.bullet_image, o.shooting_pattern, o.moving_pattern,
        o.speed, o.bullet_speed, o.hp)#'enemy01_bullet.png', 4, 0, 100, 3, 10)
    gfw.world.add(gfw.layer.enemy, obj)

    index += 1

def draw():
    pass

def load(file):
    pass