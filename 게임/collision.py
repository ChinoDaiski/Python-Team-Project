

# 플레이어와 적의 탄
# 플레이어의 탄과 적
# 의 충동체크를 하는 모듈


import gfw


def enter():
    pass

def draw():
    pass

def update():
    pass

def check_collision():
    # player의 탄과 enemy의 충동 판정
    for player_bullet in gfw.world.objects_at(gfw.layer.bullet):
        for enemy in gfw.world.objects_at(gfw.layer.enemy):
            if collides_distance(player_bullet, enemy):
                enemy.getDamage(gfw.world.object(gfw.layer.player, 0).power)
                gfw.world.remove(player_bullet)

    # enemy의 탄과 player의 충돌 판정
    for enemy_bullet in gfw.world.objects_at(gfw.layer.enemy_bullet):
        for player in gfw.world.objects_at(gfw.layer.player):
            if collides_distance(player, enemy_bullet):
                player.destroy()
                gfw.world.remove(enemy_bullet)



# 충돌 처리를 위한 함수
def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    
    radius_sum = a.radius + b.radius
    
    # 제곱근은 구하는것은 시간이 오래걸리므로 서로 제곱을 하여 연산결과를 비교한다.
    return distance_sq < radius_sum ** 2



# 충돌 처리를 위한 함수
def collides_distance2(ax, ay, radius_a, bx, by, radius_b):
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    
    radius_sum = radius_a + radius_b
    
    # 제곱근은 구하는것은 시간이 오래걸리므로 서로 제곱을 하여 연산결과를 비교한다.
    return distance_sq < radius_sum ** 2