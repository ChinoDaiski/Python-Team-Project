
# 옵션 설정을 위한 state
# 사운드 관련 옵션을 설정한다.

from pico2d import *
import gfw
import button

import stage_01
import manual_state
import option_state
import quit_state


resource = 'res/'

selectNum = 0
btnArr = []

# volume 20 / 100 / 255

def enter():

    mapX, mapY = get_canvas_width(), get_canvas_height()
    btnStartPosX = mapX // 20
    btnStartPosY = mapY // 20
    btnWidth = mapX // 4
    btnHeight = mapY // 5
    
    # 월드에 bg, ui 추가
    gfw.world.init(['bg','ui'])

    # bg 설정
    global bg, bg_2, bg_3
    bg = gfw.image.load(resource + 'bg_title.png')
    bg_2 = gfw.image.load(resource + 'bg_manual.png')
    
    for n in range(52):
        bg_3 = gfw.image.load(resource + 'snow/snow%d.png' % n)

    global frame
    frame = 0

    global bg_sound
    bg_sound = gfw.image.load(resource + '소리설정.png')

    # ui 설정
    global btnArr
    small = button.btn01(resource + 'small.png', btnStartPosX, btnStartPosY * 10, btnWidth, btnHeight, None, False, True, 2)
    btnArr.append(small)
    
    medium = button.btn01(resource + 'medium.png', btnStartPosX * 5, btnStartPosY * 7, btnWidth, btnHeight, None, False, False, 2)
    btnArr.append(medium)
    
    big = button.btn01(resource + 'big.png', btnStartPosX, btnStartPosY * 4, btnWidth, btnHeight, None, False, True, 2)
    btnArr.append(big)

    gfw.world.add(gfw.layer.ui, btnArr)
    

    global selectNum
    selectNum = 0

    volume = gfw.world.getSound()
    if volume == 100:
        selectNum = 1
        medium.bSelect = True

    elif volume == 20:
        selectNum = 0
        small.bSelect = True

    elif volume == 255:
        selectNum = 2
        big.bSelect = True

    else:
        selectNum = 0
        small.bSelect = True


    # 소리 설정
    global sound_btn

    sound_btn = load_music(resource + 'sound_switch.mp3')
    sound_btn.set_volume(255)
    
def update():
    global frame, bg_3
    frame += gfw.delta_time * 10
    frame = frame % 52
    bg_3 = gfw.image.load(resource + 'snow/snow%d.png' % (int)(frame))

    for btn in btnArr:
        btn.update()

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
    
    for btn in btnArr:
        btn.draw()

    global bg_sound
    bg_sound.clip_draw_to_origin(0, 0, bg_sound.w, bg_sound.h, get_canvas_width() // 5, get_canvas_height() // 7 * 5, get_canvas_width() // 4, get_canvas_height() // 4)

def handle_event(e):
    global selectNum
    global btnArr
    global sound_btn

    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        exit()
        gfw.pop()

    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_UP:
            if selectNum == 0:
                pass
            else:
                btnArr[selectNum].bSelect = False
                selectNum -= 1
                btnArr[selectNum].bSelect = True
                sound_btn.play()

        elif e.key == SDLK_DOWN:
            if selectNum == 2:
                pass
            else:
                btnArr[selectNum].bSelect = False
                selectNum += 1
                btnArr[selectNum].bSelect = True
                sound_btn.play()

        elif e.key == 13:

            if selectNum == 0:
                gfw.world.setSound(20)

            if selectNum == 1:
                gfw.world.setSound(100)

            if selectNum == 2:
                gfw.world.setSound(255)
                
            sound_btn.play()
        
                

def exit():
    btnArr.clear()

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()