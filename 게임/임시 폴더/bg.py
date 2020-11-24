from pico2d import *
import gfw


def init(p):
    global space, stars
    space = gfw.image.load('res/outerspace.png')
    stars = gfw.image.load('res/stars.png')

    global player
    player = p

def enter():
    pass


def update():
    pass


def draw():
    x, y = get_canvas_width() // 2, get_canvas_height() // 2
    
    # 플레이어의 위치
    px, py = player.pos
    # 플레이어와 화면 중심과의 거리
    dx, dy = x - px, y - py

    # 플레이어가 떨어져 있는 거리의 2%, 5%만큼 이동하여 그리기 (소량으로 움직이는것 처럼 보이기)
    space.draw(x + dx * 0.02, y + dy * 0.02)
    stars.draw(x + dx * 0.05, y + dy * 0.05)
