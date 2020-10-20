
from pico2d import *
import gfw.gfw
import game_state

resource = 'resource/'


def enter():
    global image
    image = load_image(resource + 'title.png')

def update():
    pass

def late_update():
    pass

def draw():
    image.draw(300, 400)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.gfw.push(game_state)
        
def exit():
    global image
    del image

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.gfw.run_main()
 