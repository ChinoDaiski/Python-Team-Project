

from gfw.gfw import *
from Player import *
from Background import *
from pico2d import *


def enter():
    global player
    global backgrond

    player = Player()
    backgrond = Backgrond()


def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.gfw.pop()

    player.handle_event(e)


def draw():
    backgrond.draw()
    player.draw()


def update():
    backgrond.update()
    player.update()


def late_update():
    backgrond.late_update()
    player.late_update()


def exit():
    pass


if __name__ == '__main__':
    gfw.gfw.run_main()