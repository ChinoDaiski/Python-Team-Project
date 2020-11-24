from pico2d import *
import gfw


MOVE_PPS = 300

def init():
    # 플레이어 이미지 초기화
    global image
    image = gfw.load_image('res/player.png')

    # 플레이어 움직임 관련 초기화
    global delta_x, delta_y, pos
    pos = get_canvas_width()//2, get_canvas_height()//2
    delta_x, delta_y = 0, 0

    global radius
    radius = image.w // 2

def enter():
    pass

def update():
    global pos
    x, y = pos
    # 이번 프레임에 움직이는 양, delta_time으로 일괄적으로 조정
    x += delta_x * MOVE_PPS * gfw.delta_time
    y += delta_y * MOVE_PPS * gfw.delta_time

    #x = min(30, max(get_canvas_width() - 30, x))

    # 이미지의 가로 세로 길이를 받아온다.
    hw, hh = image.w // 2, image.h //2

    x = clamp(hw, x, get_canvas_width() - hw)
    y = clamp(hh, y, get_canvas_height() - hh)

    pos = x, y


def late_update():
    pass

def draw():
    # 플레이어 그리기
    image.draw(*pos)

def handle_event(e):
    global delta_x, delta_y

    # 누를 경우
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_LEFT:
            delta_x -= 1
        elif e.key == SDLK_RIGHT:
            delta_x += 1
        elif e.key == SDLK_UP:
            delta_y += 1
        elif e.key == SDLK_DOWN:
            delta_y -= 1

    # 눌렀다 땔 경우
    elif e.type == SDL_KEYUP:
        if e.key == SDLK_LEFT:
            delta_x += 1
        if e.key == SDLK_RIGHT:
            delta_x -= 1
        elif e.key == SDLK_UP:
            delta_y -= 1
        elif e.key == SDLK_DOWN:
            delta_y += 1


