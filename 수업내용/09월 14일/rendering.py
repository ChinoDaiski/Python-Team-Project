from pico2d import *

import os

open_canvas()

grass = load_image('..\\image\\grass.png')
character = load_image('..\\image\\character.png')

x=0
while (x<800):
# game rendering
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
# game logic
    x = x+2
    delay(0.01)

close_canvas()