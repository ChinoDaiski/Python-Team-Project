
# 총알 클래스

# 자신의 이미지와 위치, 반지름, 속도, 움직이는 방향을 가지고 있다.
# 해당 총알은 맵 밖을 벗어나면 삭제된다.


from pico2d import *
import gfw
from math import *

MOVE_PPS = 200
Bullet_Size = 24, 30

class Bullet:
    def __init__(self, image, kinds, x, y, speed, direction, alpha):
        # 총알의 이미지, 종류, 위치, 스피드, 이동 방향를 인자로 받음
        self.image = gfw.load_image(image)
        self.kind = kinds
        self.pos = x, y
        self.speed = speed
        self.direction = direction # 이동 방향은 각도를 의미한다.
        
        # 충돌 처리를 위한 반지름
        self.radius = self.image.w // 2

        # 화면 밖을 나가면 소멸
        self.bb_left = -self.image.w
        self.bb_bottom = -self.image.h
        self.bb_right = get_canvas_width() // 7 * 5 + self.image.w
        self.bb_top = get_canvas_height() + self.image.h

        self.alpha = alpha


    def update(self):
        x, y = self.pos
        dx, dy = self.speed * cos(self.direction * pi / 180), self.speed * sin(self.direction * pi / 180)
        
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        
        self.pos = x, y

        if self.out_of_screen():
            gfw.world.remove(self)

    def draw(self):

        SDL_SetTextureBlendMode(self.image.texture, SDL_BLENDMODE_BLEND)
        SDL_SetTextureAlphaMod(self.image.texture, self.alpha)
        x, y = self.pos
        x -= Bullet_Size[0] // 2
        y -= Bullet_Size[1] // 2
        Pos = x, y
        self.image.clip_draw_to_origin(0, 0, self.image.w, self.image.h, *Pos, *Bullet_Size)

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
