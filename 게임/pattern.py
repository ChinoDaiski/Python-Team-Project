
# 탄을 만드는 class 여기서 종류별로 탄막 패턴을 만든다.


from pico2d import *
import gfw
import bullet
import generator

# stage
import stage_01


player_bullet_speed = 3
enemy_bullet_speed = 1

resource = 'res/'

Pattern = [ 'player', 'enemy', 'boss' ]

# 플레이어 탄막 구성 정보
# player
# player_round
# player_n_way


def init():
    pass

def update():
    pass

def fire_pattern(pattern_Name, n, x, y):
    pos = x, y

    # 플레이어가 총을 쏘는 패턴일 경우
    #==================================================================================================================
    if pattern_Name == 'player':
        # image, kinds, pos, speed, direction
        blt = bullet.Bullet(resource + 'bullet_player_sub.png', *pos, player_bullet_speed, 90, 100)
        gfw.world.add(gfw.layer.bullet, blt)

    elif pattern_Name == 'player_round':
        # image, kinds, pos, speed, direction
        for n in range(60):
            blt = bullet.Bullet(resource + 'bullet_player_sub.png', *pos, player_bullet_speed, 360 // 60 * n, 100)
            gfw.world.add(gfw.layer.bullet, blt)
        
    elif pattern_Name == 'player_n_way':
        # image, kinds, pos, speed, direction
        for n in range(20):
            blt = bullet.Bullet(resource + 'bullet_player_sub.png', *pos, player_bullet_speed, 90 / 20 * n + 45, 100)
            gfw.world.add(gfw.layer.bullet, blt)
    #==================================================================================================================
        




    # 적이 총을 쏘는 패턴일 경우

    #==================================================================================================================
    # stage01 일반
    #==================================================================================================================
    # 360도 기준으로 n개 발사
    elif pattern_Name == 'enemyNormal_1':
        for i in range(n):
            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, 360 / n * i, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 아랫부분으로 180도 기준으로 n개 발사
    elif pattern_Name == 'enemyNormal_2':
        for i in range(n):
            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, 90 / n * i + 45 + 180, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 플레이어를 향해 n개 발사
    elif pattern_Name == 'enemyNormal_3':
        for i in range(n):
            player = gfw.world.object(gfw.layer.player, 0)
            px, py = player.pos
            degree = get_degree(x, y, px, py)

            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, degree, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 플레이어를 향해 n개 넓게 발사
    elif pattern_Name == 'enemyNormal_4':
        for i in range(n + 1):
            player = gfw.world.object(gfw.layer.player, 0)
            px, py = player.pos
            degree = get_degree(x, y, px, py)
            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, degree - 90 + 180 / n * i, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)
    #==================================================================================================================
    # stage01 보스
    #==================================================================================================================
    # 플레이어를 향해 n개 발사
    elif pattern_Name == 'enemyBoss_phase01_1':
        for i in range(n):
            player = gfw.world.object(gfw.layer.player, 0)
            px, py = player.pos
            degree = get_degree(x, y, px, py)
            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, degree, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 원 형태로 n개 발사
    elif pattern_Name == 'enemyBoss_phase02_1':
        for i in range(n):
            player = gfw.world.object(gfw.layer.player, 0)
            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, 360 / n * i, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 플레이어 방향으로 방사형으로 발사
    elif pattern_Name == 'enemyBoss_phase02_1':
        # 방사각도 나중에 인자로 받기 추가
        Radiation_angle = 90
        for i in range(n + 1):
            player = gfw.world.object(gfw.layer.player, 0)
            px, py = player.pos
            degree = get_degree(x, y, px, py)
            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, degree - Radiation_angle + Radiation_angle * 2 / n * i, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 발사한 탄을 특정 패턴으로 이동
    elif pattern_Name == 'enemyBoss_phase02_2':
        for i in range(n):
            pass
    #==================================================================================================================


# 인자로 현재 위치(x, y)와 도착 위치(px, py)를 받아 두 점 사이의 각도를 반환하는 함수
def get_degree(x, y, px, py):
    dx = px - x
    dy = py - y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if distance == 0:
        return 0

    if dx == 0:
        dx = 0.0000001
    if dy == 0:
        dy = 0.0000001
    
    dx, dy = dx / distance, dy / distance
    angle = math.atan2(dy, dx) / math.pi * 180
    
    return angle