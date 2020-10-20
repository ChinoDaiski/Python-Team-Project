import gfw.gfw
from pico2d import *
import title_state

resource = 'resource/'

def enter():
    global image, elapsed
    image = load_image(resource + 'logo.png')
    elapsed = 0

def update():
    global elapsed
    elapsed += gfw.gfw.delta_time
    print(elapsed)
    if elapsed > 1.0:
        gfw.gfw.change(title_state)

def late_update():
    pass

def draw():
    image.draw(300, 400)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.gfw.quit()

def exit():
    global image
    del image

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.gfw.run_main()
