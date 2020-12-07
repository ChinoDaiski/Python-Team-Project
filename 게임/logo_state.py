
# 게임을 시작하는 곳
# 각종 로고가 뜨고 게임의 기능을 선택하는 곳으로 넘어간다.


from pico2d import *
import gfw
import title_state

resource = 'res/'
time = 4.0

def enter():
    global image, elapsed
    image = gfw.image.load(resource + 'logo01.png')
    elapsed = 0

    global logo01, logo02, logo03
    logo01 = False
    logo02 = False
    logo03 = False

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
    global logo01, logo02, logo03

    if logo01 == False:
        if elapsed >= time:
            gfw.image.unload(resource + 'logo01.png')
            image = gfw.image.load(resource + 'logo02.png')
            elapsed = 0.0
            logo01 = True

    elif logo02 == False:
        if elapsed >= time:
            gfw.image.unload(resource + 'logo02.png')
    #       image = gfw.image.load(resource + 'logo03.png')
    #         elapsed = 0.0
    #         logo02 = True

    # elif logo03 == False:
    #      if elapsed >= time:
    #          gfw.image.unload(resource + 'logo03.png')
    #          logo03 = True
            gfw.change(title_state)

    #print(alpha)

def late_update():
    pass

def draw():
    bg.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())

    global alpha
    SDL_SetTextureBlendMode(image.texture, SDL_BLENDMODE_BLEND)
    SDL_SetTextureAlphaMod(image.texture, int(alpha))

    image.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width()   , get_canvas_height())

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

def exit():
    global image
    del image

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
