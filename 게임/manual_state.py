
# 메뉴얼 설정을 위한 state
# 이곳에서 게임의 간단한 예시를 보여준다.

from pico2d import *
import gfw
import button

import stage_01
import manual_state
import option_state
import quit_state


resource = 'res/'

# volume 20 / 100 / 255

def enter():
    
    # 월드에 bg, ui 추가
    gfw.world.init(['bg','ui'])

    global Font_big
    Font_big = gfw.font.load(resource + 'BinggraeSamanco-Bold.ttf', get_canvas_height() // 7)
    global Font_small
    Font_small = gfw.font.load(resource + 'BinggraeSamanco-Bold.ttf', get_canvas_height() // 20)

    # bg 설정
    global bg, bg_2, bg_3
    bg = gfw.image.load(resource + 'bg_title.png')
    bg_2 = gfw.image.load(resource + 'bg_option.png')
    
    for n in range(52):
        bg_3 = gfw.image.load(resource + 'snow/snow%d.png' % n)

    global frame
    frame = 0

    # 소리 설정
    global sound_btn
    sound_btn = load_music(resource + 'sound_switch.mp3')
    sound_btn.set_volume(255)
    
def update():
    global frame, bg_3
    frame += gfw.delta_time * 10
    frame = frame % 52
    bg_3 = gfw.image.load(resource + 'snow/snow%d.png' % (int)(frame))

def setAlpha(image, alpha):
    SDL_SetTextureBlendMode(image.texture, SDL_BLENDMODE_BLEND)
    SDL_SetTextureAlphaMod(image.texture, alpha)

def draw():

    bg.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())
    
    global bg_3

    setAlpha(bg_3, 255)
    bg_2.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())

    setAlpha(bg_3, 30)
    bg_3.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())


    global Font_big, Font_small

    Font_big.draw(get_canvas_width() // 8, get_canvas_height() // 8 * 7, '움직임')
    Font_small.draw(get_canvas_width() // 6, get_canvas_height() // 8 * 6, '방향키를 사용해서 캐릭터를 움직일 수 있습니다.')

    Font_big.draw(get_canvas_width() // 8, get_canvas_height() // 8 * 5, '공격')
    Font_small.draw(get_canvas_width() // 6, get_canvas_height() // 8 * 4, 'z키를 눌려 공격을 할 수 있습니다.')

    Font_big.draw(get_canvas_width() // 8, get_canvas_height() // 8 * 3, '폭탄')
    Font_small.draw(get_canvas_width() // 6, get_canvas_height() // 8 * 2, 'x키를 눌러 폭탄을 사용할 수 있습니다.')

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        exit()
        gfw.pop()
        
                

def exit():
    pass

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()