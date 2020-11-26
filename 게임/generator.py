# 미사일을 지속하여 생성하는 모듈

from pico2d import *
import gfw
import random as r

from bullet import Bullet
from enemy import enemy_Nomal
import pattern


MISSILE_COUNT = 10
SPEED = 10
# 적 스프라이트, <- 프레임 인덱스 길이, 파괴 스프라이트, <- 프레임 인덱스 길이, 위치(x, y), 탄 이미지, 공격 패턴
# image, fidx, image_destroy, d_fidx, x, y, bullet_image, pattern


enemy_Info = [
    [ 'enemy01.png', 12, 'enemy01_bomb.png', 8, 0, 0, 'enemy01_bullet.png', 0, 100 ],
    [ 'enemy01.png', 12, 'enemy01_bomb.png', 8, 0, 0, 'enemy01_bullet.png', 0, 100 ]
]

def init():
    map_size = gfw.world.getMapSize()
    global mw, mh
    mw = map_size[0]
    mh = map_size[1]

    global delta_time
    delta_time = 0

def update():
    global delta_time
    delta_time += gfw.delta_time
    if delta_time > 2.0:
        x = []
        for n in range(3):
            x.append(300 * n)
        #generate_enemy(0, x)
        delta_time = 0.0



# # 오브젝트를 인자로 받아 탄을 생성하여 bullet layer에 넣어주는 함수
# def generate_bullet(objectName, pattern_name, x, y):
#     bullet = pattern.fire_pattern(pattern_name, x, y)
#     if not len(bullet) == 0:
#         for n in range(len(bullet)):
#             if objectName == 'enemy':
#                 gfw.world.add(gfw.layer.enemey_bullet, bullet[n])
#             elif objectName == 'player':
#                 gfw.world.add(gfw.layer.bullet, bullet[n])
#     else:
#         if objectName == 'enemy':
#             gfw.world.add(gfw.layer.enemey_bullet, bullet[n])
#         elif objectName == 'player':
#             gfw.world.add(gfw.layer.bullet, bullet[n])


# 적의 종류와 숫자 및 숫자 만큼의 x값를 인자로 받아 (x, 맵 맨위) 에서 적을 생성하는 함수
def generate_enemy(kinds, list):
    Num = len(list)
    for n in range(Num):
        e = enemy_Info[0]
        e[4] = list[n]
        enemy = enemy_Nomal(*e)
        gfw.world.add(gfw.layer.enemy, enemy)