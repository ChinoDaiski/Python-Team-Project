
# 게임의 기능을 선택하는 곳
# 게임의 시작, 메뉴얼, 옵션, 나가기 4가지 기능을 선택할 수 있다.

# 시작시 stage 01로 넘어간다.
# 메뉴얼시 기능에 대한 설명이 있는 장면을 보여준다.
# 옵션을 선택하면 사운드 설정 및 라이프 설정을 할 수 있는 곳으로 간다.
# 나가기를 선택하면 게임이 종료된다.


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

def enter():

    mapX, mapY = get_canvas_width(), get_canvas_height()
    btnStartPosX = mapX // 20
    btnStartPosY = mapY // 20
    btnWidth = mapX // 4
    btnHeight = mapY // 5
    
    # 월드에 bg, ui 추가
    gfw.world.init(['bg','ui'])

    # bg 설정
    global bg, bg_2, bg_3, GameName
    bg = gfw.image.load(resource + 'bg_title.png')
    bg_2 = gfw.image.load(resource + 'bg_title2.png')
    
    for n in range(52):
        bg_3 = gfw.image.load(resource + 'snow/snow%d.png' % n)
    global frame
    frame = 0

    GameName = gfw.image.load(resource + 'GameName01.png')

    # ui 설정
    global btnArr
    GameStart = button.btn(resource + 'GameStart.png', btnStartPosX, btnStartPosY * 10, btnWidth, btnHeight, None, True, 'stage01', True)
    btnArr.append(GameStart)
    
    Manual = button.btn(resource + 'Manual.png', btnStartPosX * 5, btnStartPosY * 7, btnWidth, btnHeight, None, False, 'manual_state', False)
    btnArr.append(Manual)
    
    Option = button.btn(resource + 'Option.png', btnStartPosX, btnStartPosY * 4, btnWidth, btnHeight, None, False, 'option_state', True)
    btnArr.append(Option)
    
    Quit = button.btn(resource + 'Quit.png', btnStartPosX * 5, btnStartPosY * 1, btnWidth, btnHeight, None, False, 'quit_state', False)
    btnArr.append(Quit)

    gfw.world.add(gfw.layer.ui, btnArr)
    
    global selectNum
    selectNum = 0

    global bg_music, sound_btn
    bg_music = load_wav(resource + 'TitleState_background.wav')
    if gfw.world.getSound() == 0:
        bg_music.set_volume(50)
    else:
        bg_music.set_volume(gfw.world.getSound())

    sound_btn = load_music(resource + 'sound_switch.mp3')
    sound_btn.set_volume(255)

    bg_music.play()
    
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
    global bg_3

    bg.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())
    
    setAlpha(bg_3, 255)
    bg_2.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())

    setAlpha(bg_3, 30)
    bg_3.clip_draw_to_origin(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, get_canvas_width(), get_canvas_height())

    setAlpha(GameName, 255)
    GameName.clip_draw_to_origin(0, 0, GameName.w, GameName.h, get_canvas_width() - GameName.w, 0, GameName.w, GameName.h)
    
    for btn in btnArr:
        btn.draw()

def handle_event(e):
    global selectNum
    global btnArr


    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

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
            if selectNum == 3:
                pass
            else:
                btnArr[selectNum].bSelect = False
                selectNum += 1
                btnArr[selectNum].bSelect = True
                sound_btn.play()

        elif e.key == 13:
            sound_btn.play()

            if selectNum == 0:
                bg_music.stop()
                gfw.push(stage_01)

            if selectNum == 1:
                gfw.push(manual_state)

            if selectNum == 2:
                gfw.push(option_state)

            if selectNum == 3:
                bg_music.stop()
                gfw.push(quit_state)
                

def exit():
    pass

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()