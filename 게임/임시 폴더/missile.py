from pico2d import *
import gfw


MOVE_PPS = 200

class Missile:
    def __init__(self, pos, delta):
        self.pos = pos
        self.delta = delta
        self.image = gfw.load_image('res/missile.png')

        self.bb_left = -self.image.w
        self.bb_bottom = -self.image.h
        self.bb_right = get_canvas_width() + self.image.w
        self.bb_top = get_canvas_height() + self.image.h
        
        self.radius = self.image.w // 2


    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        
        self.pos = x, y

        if self.out_of_screen():
            gfw.world.remove(self)



    def draw(self):
        self.image.draw(*self.pos)


    def out_of_screen(self):
        x, y = self.pos

        if x < self.bb_left :
            return True
        elif x > self.bb_right :
            return True
        elif y > self.bb_top :
            return True
        elif y < self.bb_bottom :
            return True


        return False
