
# 종료 여부를 물어보는 state

from pico2d import *
import gfw
import title_state

resource = 'res/'
time = 5.0

def enter():
    global image, elapsed
    image = gfw.image.load(resource + 'bg_quit.png')
    elapsed = 0

    global logo01
    logo01 = False

    global alpha, cli
    alpha = 0
    cli = False

    global bg
    bg = gfw.image.load(resource + 'bg_black.png')

def update():
    
    global alpha, cli
    delta_time = gfw.delta_time

    ALPHA_SIZE = 510 * delta_time / time

    if cli == False:
        if alpha < 255:
            alpha += ALPHA_SIZE
        
        if alpha >= 255:
            cli = True
            alpha = 255

    elif cli == True:
        alpha -= ALPHA_SIZE
        if alpha <= 0:
            cli = False
            alpha = 0


    global elapsed
    elapsed += delta_time
    
    global image
    global logo01

    if logo01 == False:
        if elapsed >= time:
            gfw.image.unload(resource + 'logo01.png')
            image = gfw.image.load(resource + 'logo02.png')
            elapsed = 0.0
            logo01 = True
            gfw.quit()

    #print(alpha)

def late_update():
    pass

def draw():
    bg.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())

    global alpha
    SDL_SetTextureBlendMode(image.texture, SDL_BLENDMODE_BLEND)
    SDL_SetTextureAlphaMod(image.texture, int(alpha))

    image.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())

def handle_event(e):
    pass

def exit():
    global image
    del image

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
