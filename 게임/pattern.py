
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
    # 360도 기준으로 n개 발사
    elif pattern_Name == 'enemyNormal_01':
        for i in range(n):
            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, 360 / n * i, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 아랫부분으로 180도 기준으로 n개 발사
    elif pattern_Name == 'enemyNormal_02':
        for i in range(n):
            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, 90 / n * i + 45 + 180, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)

    # 플레이어를 향해 n개 발사
    elif pattern_Name == 'enemyNormal_03':
        for i in range(n):
            player = gfw.world.object(gfw.layer.player, 0)
            x, y = player.pos



            blt = bullet.Bullet(resource + 'bullet_player.png', *pos, enemy_bullet_speed, 90 / n * i + 45 + 180, 100)
            gfw.world.add(gfw.layer.enemy_bullet, blt)
    #==================================================================================================================

def get_degree(x, y, px, py):
    dx = px - x
    dy = py - y
    return math.atan(dy / dx)