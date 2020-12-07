# 미사일을 지속하여 생성하는 모듈

from pico2d import *
import gfw
import random as r

from bullet import Bullet
import enemy
import pattern


MISSILE_COUNT = 10
SPEED = 10
# 적 스프라이트, <- 프레임 인덱스 길이, 파괴 스프라이트, <- 프레임 인덱스 길이, 위치(x, y), 탄 이미지, 공격 패턴
# image, fidx, image_destroy, d_fidx, x, y, bullet_image, pattern


    # 01. 자신의 이미지
    # 02. 이미지 최대 x, y프레임
    # 03. 파괴 이미지
    # 04. 파괴 이미지 최대 x, y프레임
    # 05. 시작 위치
    # 06. 도착 위치
    # 07. 탄 이미지
    # 08. 탄을 발사하는 패턴 번호
    # 09. 움직이는 패턴 번호
    # 10. 스피드
enemy_Info = [
    [ 'enemy01.png', 12, 1, 'enemy01_bomb.png', 5, 5, 0, 0, 'enemy01_bullet.png', 0, 0, 100 ],
    [ 'enemy02.png', 12, 1, 'enemy01_bomb.png', 5, 5, 0, 0, 'enemy01_bullet.png', 0, 0, 100 ]
]

enemy_Info_list = []

def init():
    # 패턴 모듈 init
    pattern.init()

    global Tile, hz, vt
    Tile = pattern.getTile()
    hz, vt = pattern.getTileCount()
    # ...
    #  3,-1  3,0  3,1 ...
    #  2,-1  2,0  2,1 ...
    #  1,-1  1,0  1,1 ...
    #  0,-1  0,0  0,1 ...
    # -1,-1 -1,0 -1,1 ... <- 첫번째 줄, 리스트 인덱스 [0][0]부터 시작


    map_size = gfw.world.getMapSize()
    global mw, mh
    mw = map_size[0]
    mh = map_size[1]

    global delta_time
    delta_time = 0

    # image, Mfidx, Mfidy, image_destroy, d_Mfidx, d_Mfidy, last_line_image_count, start_x, start_y, dst_x, dst_y, bullet_image, fire_pattern, move_pattern, speed, bullet_speed, hp
    for i in range(hz):
        for j in range(hz):
            Info = ['enemy01.png', 12, 1, 'enemy01_bomb.png', 5, 5, 1, Tile[hz][i][0], Tile[hz][i][1], Tile[0][j][0], Tile[0][j][1], 'enemy01_bullet.png', 1, 1, 200, 300, 10]
            enemy_Info_list.append(Info)
    
    # for emy in enemy_Info_list:
    #     print(*emy)
    global gen
    gen = False

def update():
    global delta_time, gen
    delta_time += gfw.delta_time
    if delta_time > 1.0 and not gen:
        lst = generate_enemy(1, 1, 1)
        for n in lst:
            emy = enemy.enemy_Nomal(*n)
            gfw.world.add(gfw.layer.enemy, emy)
        
        gen = True
    

# 적이 움직이는 방법과 숫자와 공격 방식을 인자로 받는 함수, 해당 인자롤 받아 적의 정보를 생성해낸다.
def generate_enemy(wayPoint, Count, attack_pattern):
    global Tile, hz, vt

    hz -= 1
    vt -= 1

    Num = Count
    Info = []
    Info_list = []
    # 아래로 내려가는 방법
    if wayPoint == 1:

    # 01. 자신의 이미지
    # 02. 이미지 최대 x, y프레임
    # 03. 파괴 이미지
    # 04. 파괴 이미지 최대 x, y프레임, 마지막 줄의 이미지 숫자
    # 05. 시작 위치
    # 06. 도착 위치
    # 07. 탄 이미지
    # 08. 탄을 발사하는 패턴 번호
    # 09. 움직이는 패턴 번호
    # 10. 스피드
    # 11. 탄의 스피드
    # 12. 체력
    # 13. MOVE_PPS
        for n in range(Num):
            Info = ['enemy01.png', 12, 1, 'enemy01_bomb.png', 5, 5, 1, Tile[vt][round(hz / (Num + 1) * (n + 1))][0], Tile[vt][hz][1], Tile[vt][round(hz / (Num + 1) * (n + 1))][0], Tile[0][0][1], 'enemy01_bullet.png', 1, 1, 100, 2, 10, 2]
            Info_list.append(Info)
            

    # 좌하단으로 꺽는 방법
    if wayPoint == 2:
        pass
    # 우하단으로 꺾는 방법
    if wayPoint == 3:
        pass
    # 좌상단으로 꺽는 방법
    if wayPoint == 4:
        pass
    # 우상단으로 꺽는 방법
    if wayPoint == 5:
        pass
    
    # 왼쪽을 중심으로 아래로 베지어 이동하는 방법
    if wayPoint == 6:
        pass
    # 오른쪽을 중심으로 아래로 베지어 이동하는 방법
    if wayPoint == 7:
        pass
    # 왼쪽을 중심으로 위로 베지어 이동하는 방법
    if wayPoint == 8:
        pass
    # 오른쪽을 중심으로 위로 베지어 이동하는 방법
    if wayPoint == 9:
        pass


    hz += 1
    vt += 1

    return Info_list

















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
