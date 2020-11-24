from pico2d import *
import gfw
import generator
import player
import bg

# 충돌 처리를 위한 함수
def collides_distance(a, b):
    ax, ay = a.pos
    bx, by = b.pos
    distance_sq = (ax - bx) ** 2 + (ay - by) ** 2
    
    radius_sum = a.radius + b.radius
    
    # 제곱근은 구하는것은 시간이 오래걸리므로 서로 제곱을 하여 연산결과를 비교한다.
    return distance_sq < radius_sum ** 2

def check_collision():
    for m in gfw.world.objects_at(gfw.layer.missile):
        # 충돌이 일어날 경우
        if collides_distance(player, m):
            gfw.world.remove(m)


def enter():
    gfw.world.init(['bg','missile','player'])

    generator.init()

    bg.init(player)
    gfw.world.add(gfw.layer.bg, bg)

    player.init()
    gfw.world.add(gfw.layer.player, player)

def exit():
    pass

def update():
    gfw.world.update()
    generator.update()
    check_collision()

def late_update():
    pass

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        
    # 이벤트 넘기기
    player.handle_event(e)


if __name__ == '__main__':
    gfw.run_main()