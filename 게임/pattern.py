
# 탄을 만드는 class 여기서 종류별로 탄막 패턴을 만든다.


from pico2d import *
import gfw
import bullet
import generator

# stage
import stage_01


player_bullet_speed = 4

resource = 'res/'

Pattern = [ 'player', 'enemy', 'boss' ]

# 플레이어 탄막 구성 정보
# player
# player_round
# player_n_way


def init():
    pass

def fire_pattern(pattern_Name, x, y):
    pos = x, y
    blt = []

    # 플레이어가 총을 쏘는 패턴일 경우
    if pattern_Name == 'player':
        # image, kinds, pos, speed, direction
        blt.append(bullet.Bullet(resource + 'bullet_player_sub.png', 'player', *pos, player_bullet_speed, 90, 100))
        #gfw.world.add(gfw.layer.bullet, bullet)
        return blt

    elif pattern_Name == 'player_round':
        # image, kinds, pos, speed, direction
        for n in range(30):
            blt.append(bullet.Bullet(resource + 'bullet_player.png', 'player', *pos, player_bullet_speed, 360 // 30 * n, 100))
        #gfw.world.add(gfw.layer.bullet, bullet)
        return blt
        
    elif pattern_Name == 'player_n_way':
        # image, kinds, pos, speed, direction
        for n in range(20):
            blt.append(bullet.Bullet(resource + 'bullet_player.png', 'player', *pos, player_bullet_speed, 90 / 20 * n + 45, 100))
        #gfw.world.add(gfw.layer.bullet, bullet)
        return blt
        

