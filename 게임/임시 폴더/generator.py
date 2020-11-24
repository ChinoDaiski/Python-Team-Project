# 미사일을 지속하여 생성하는 모듈

from pico2d import *
import gfw
import random as r
# 미사일 모듈을 받아온다
from missile import Missile


MISSILE_COUNT = 10
SPEED = 10


def init():
    pass

def update():
    if gfw.world.count_at(gfw.layer.missile) < MISSILE_COUNT:
        generate()


def generate():
    # 튜플로 묶어서 보내기
    x, y, dx, dy = get_coords()
    m = Missile((x, y), (dx, dy))
    gfw.world.add(gfw.layer.missile, m)


def get_coords():
    x = r.randrange(get_canvas_width())
    y = r.randrange(get_canvas_height())
    dx = r.random()
    dy = r.random()

    if dx < 0.5:
        dx -=1

    if dy < 0.5:
        dy -=1

    side = r.randint(1, 4)

    if side == 1: # left
        x = 0

    elif side == 2: # bottom
        y = 0

    if side == 3: # right
        x = get_canvas_width()

    elif side == 4: # top
        y = get_canvas_height()


    return x, y, dx, dy