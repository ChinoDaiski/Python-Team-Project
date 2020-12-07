
# 탄을 만드는 class 여기서 종류별로 탄막 패턴을 만든다.


from pico2d import *
import gfw
import bullet
import function
import generator


# stage
import stage_01


player_bullet_speed = 4
enemy_bullet_speed = 3

resource = 'res/'


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
enemy01 = { 'image' : 'enemy01.png',
            'Mfidx' : '12',
            'Mfidy' : '1',
            'image_destroy' : 'enemy01_bomb.png',
            'd_Mfidx' : '5',
            'd_Mfidy' : '5',
            'last_line_image_count' : '1',
            'bullet_image' : 'enemy01_bullet.png',
            'shooting_pattern' : '1',
            'moving_pattern' : '1',
            'speed' : '200',
            'bullet_speed' : '300' }

enemy02 = { 'image' : 'enemy02.png',
            'Mfidx' : '12',
            'Mfidy' : '1',
            'image_destroy' : 'enemy02_bomb.png',
            'd_Mfidx' : '5',
            'd_Mfidy' : '5',
            'last_line_image_count' : '1',
            'bullet_image' : 'enemy02_bullet.png',
            'shooting_pattern' : '1',
            'moving_pattern' : '1',
            'speed' : '200',
            'bullet_speed' : '300' }

# 플레이어 탄막 구성 정보
# player
# player_round
# player_n_way


Tile = []
Tile_Horizontal = 0
Tile_Vertical = 0

enemy_bullet_alpha = 0
player_bullet_alpha = 0


player_bullet_Size = 24, 30
enemy_bullet_Size = 15, 30


# 타일의 정보를 반환하는 함수
def getTile():
    global Tile
    return Tile

# 타일의 가로, 세로 길이를 반환하는 함수(실제 길이는 각각 2만큼 더 길다, 왜냐하면 처음과 끝에 1개씩 더 붙어있기 때문이다.)
def getTileCount():
    global Tile_Horizontal, Tile_Vertical
    return Tile_Horizontal + 2, Tile_Vertical + 2



def init():
    global enemy_bullet_alpha, player_bullet_alpha
    enemy_bullet_alpha = 255
    player_bullet_alpha = 150

    MAP_SIZE = gfw.world.getMapSize()
    if MAP_SIZE[0] == 0 and MAP_SIZE[1] == 0:
        MAP_SIZE = get_canvas_width() // 7 * 5, get_canvas_height()
        
    i = 8   # 타일의 가로 갯수
    j = 12  # 타일의 세로 갯수

    global Tile_Horizontal, Tile_Vertical
    Tile_Horizontal = i # 가로
    Tile_Vertical = j   # 세로

    global Tile
    # 세로 j개의 타일 + 양쪽에 1개씩 맵 밖의 위치 포함
    for vertical in range(j + 2):
        global lst
        lst = []
        # 가로 i개의 타일 + 양쪽에 1개씩 맵 밖의 위치 포함
        for horizontal in range(i + 2):
            lst.append([MAP_SIZE[0] // i * (horizontal - 1) + MAP_SIZE[0] // i // 2, MAP_SIZE[1] // j * (vertical - 1) + MAP_SIZE[1] // j // 2])
        Tile.append(lst)
    
    global bPrint
    bPrint = False

    

def update():
    global bPrint, Tile

    if not bPrint:
        for vertical in range(Tile_Vertical + 2):
            for horizontal in range(Tile_Horizontal + 2):
                pass
                #print(Tile[vertical][horizontal])
    
        bPrint = True



# 탄을 발사하는 함수
#========================
# 패턴 이름
# 탄 이미지의 이름
# 탄의 갯수
# 발사하는 오브젝트의 위치
# 탄의 스피드
#========================
# 를 인자로 받는다.
def fire_pattern(pattern_Name, image_bullet, n, x, y, bullet_speed):
    pos = x, y

    # 플레이어가 탄을 쏘는 패턴일 경우
    #==================================================================================================================
    # 직선 공격
    if pattern_Name == 'player_level_00':
        # image, kinds, pos, speed, direction
        blt = bullet.Bullet(image_bullet, *pos, *player_bullet_Size, bullet_speed, 90, player_bullet_alpha)
        gfw.world.add(gfw.layer.bullet, blt)

    # 3갈래 공격
    elif pattern_Name == 'player_level_01':
        # image, kinds, pos, speed, direction
        for n in range(3):
            px, py = pos
            px += (30 - 30 * n)
            if n % 2 == 0:
                py -= 30
            Pos = px, py
            blt = bullet.Bullet(image_bullet, *Pos, *player_bullet_Size, bullet_speed, 30 / 3 * n + 80, player_bullet_alpha)
            gfw.world.add(gfw.layer.bullet, blt)
    
    # 자동 추적 공격
    elif pattern_Name == 'player_level_02':
        # 1개는 앞으로 공격
        blt = bullet.Bullet(image_bullet, *pos, *player_bullet_Size, bullet_speed, 90, player_bullet_alpha)
        gfw.world.add(gfw.layer.bullet, blt)

        # 나머지 2개는 자동 추적
        for n in range(3):
            px, py = pos
            px += (30 - 30 * n)
            if n % 2 == 0:
                py -= 30
                
            blt = bullet.Bullet(image_bullet, *pos, *player_bullet_Size, bullet_speed, 30 / 3 * n + 80, player_bullet_alpha)
            if n == 0 or n == 2:
                # enemy 레이어에 오브젝트가 있을 경우
                p = gfw.world.count_at(gfw.layer.enemy)
                if not p == 0:
                    k = 0
                    bCheck = True
                    # enemy 레이어의 정보 중 이미 격파된 것은 넘긴다.
                    while bCheck:
                        if not gfw.world.count_at(gfw.layer.enemy) == 0:
                            obj = gfw.world.object(gfw.layer.enemy, k)
                            if obj.bShotdown:
                                k += 1
                                bCheck = False
                            else:
                                bCheck = False
                                
                        else:
                            bCheck = False

                    if gfw.world.count_at(gfw.layer.enemy) > k:
                        blt.set_target(gfw.world.object(gfw.layer.enemy, k))
                    else:
                        blt.set_target(None)

                    mapX, mapY = gfw.world.getMapSize()
                    if n == 0:
                        blt.set_Bezier(mapX, mapY // 2)
                    elif n == 2:
                        blt.set_Bezier(0, mapY // 2)


            # 없을 경우 일반 공격
            gfw.world.add(gfw.layer.bullet, blt)

    # 자동 추적 공격 2단계
    elif pattern_Name == 'player_level_03':
        # image, kinds, pos, speed, direction
        for n in range(20):
            blt = bullet.Bullet(image_bullet, *pos, *player_bullet_Size, bullet_speed, 90 / 20 * n + 45, player_bullet_alpha)
            gfw.world.add(gfw.layer.bullet, blt)
    
    # 전체 데미지 up
    elif pattern_Name == 'player_level_04':
        # image, kinds, pos, speed, direction
        for n in range(20):
            blt = bullet.Bullet(image_bullet, *pos, *player_bullet_Size, bullet_speed, 90 / 20 * n + 45, player_bullet_alpha)
            gfw.world.add(gfw.layer.bullet, blt)
    #==================================================================================================================
        




    # 적이 탄을 쏘는 패턴일 경우
    #==================================================================================================================
    # stage01 일반
    #==================================================================================================================
    # 360도 기준으로 n개 발사
    elif pattern_Name == 'enemyNormal_1':
        for i in range(n):
            blt = bullet.Bullet(image_bullet, *pos, *enemy_bullet_Size, bullet_speed, 360 / n * i, enemy_bullet_alpha)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 아랫부분으로 180도 기준으로 n개 발사
    elif pattern_Name == 'enemyNormal_2':
        for i in range(n):
            blt = bullet.Bullet(image_bullet, *pos, *enemy_bullet_Size, bullet_speed, 90 / n * i + 45 + 180, enemy_bullet_alpha)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 플레이어를 향해 n개 발사
    elif pattern_Name == 'enemyNormal_3':
        for i in range(n):
            player = gfw.world.object(gfw.layer.player, 0)
            px, py = player.pos
            degree = function.get_degree(x, y, px, py)

            blt = bullet.Bullet(image_bullet, *pos, *enemy_bullet_Size, bullet_speed, degree, enemy_bullet_alpha)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 플레이어를 향해 n개 넓게 발사
    elif pattern_Name == 'enemyNormal_4':
        for i in range(n + 1):
            player = gfw.world.object(gfw.layer.player, 0)
            px, py = player.pos
            degree = function.get_degree(x, y, px, py)
            blt = bullet.Bullet(image_bullet, *pos, *enemy_bullet_Size, bullet_speed, degree - 90 + 180 / n * i, enemy_bullet_alpha)
            gfw.world.add(gfw.layer.enemy_bullet, blt)
    #==================================================================================================================
    # stage01 보스
    #==================================================================================================================
    # 플레이어를 향해 n개 발사
    elif pattern_Name == 'enemyBoss_phase01_1':
        for i in range(n):
            player = gfw.world.object(gfw.layer.player, 0)
            px, py = player.pos
            degree = function.get_degree(x, y, px, py)
            blt = bullet.Bullet(image_bullet, *pos, *enemy_bullet_Size, bullet_speed, degree, enemy_bullet_alpha)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 원 형태로 n개 발사
    elif pattern_Name == 'enemyBoss_phase02_1':
        for i in range(n):
            player = gfw.world.object(gfw.layer.player, 0)
            blt = bullet.Bullet(image_bullet, *pos, *enemy_bullet_Size, bullet_speed, 360 / n * i, enemy_bullet_alpha)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 플레이어 방향으로 방사형으로 발사
    elif pattern_Name == 'enemyBoss_phase02_1':
        # 방사각도 나중에 인자로 받기 추가
        Radiation_angle = 90
        for i in range(n + 1):
            player = gfw.world.object(gfw.layer.player, 0)
            px, py = player.pos
            degree = function.get_degree(x, y, px, py)
            blt = bullet.Bullet(image_bullet, *pos, *enemy_bullet_Size, bullet_speed, degree - Radiation_angle + Radiation_angle * 2 / n * i, enemy_bullet_alpha)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 발사한 탄을 특정 패턴으로 이동
    elif pattern_Name == 'enemyBoss_phase02_2':
        for i in range(n):
            pass
    #==================================================================================================================


# 오브젝트를 움직이는 함수
#========================
# 패턴 이름
# 시작지점
# 도착지점
#========================
# 을 인자로 받는다.
def move_pattern(object, pattern_Name, n, x, y, px, py):
    if pattern_Name == 'moveAtoB':
        pass
    elif pattern_Name == 'bazier01':
        pass
    elif pattern_Name == 'bazier02':
        pass

# 적 오브젝트를 생성하는 함수
def generate_pattern(pattern_Name, n, x, y):
    pass

