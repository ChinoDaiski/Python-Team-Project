from pico2d import *

import os

open_canvas()

grass = load_image('..\\image\\grass.png')
character = load_image('..\\image\\run_animation.png')

x = 0
frame = 0
while (x<800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,90)
    update_canvas()
    frame=(frame+1)%8
    x+=5
    delay(0.03)
    get_events()    # 아직은 의미 없음

close_canvas()