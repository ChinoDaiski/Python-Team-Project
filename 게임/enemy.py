

# 적기에 대한 정보를 담고 있는 모듈

from pico2d import *
import gfw

# 적 이미지의 크기
enemey_size = 40, 40

# 적이 파괴되는 동안 걸리는 시간
destroy_time = 2

# 파괴하는 이미지의 크기
destroy_size = 50, 50

# 일반적인 적
# 자신의 이미지와 발사하는 탄의 이미지, 탄막의 종류가 다르다.
class enemy_Nomal:
    def __init__(self, image, fidx, image_destroy, d_fidx, x, y, bullet_image, pattern):
        self.pos = x, y
        self.image = gfw.image.load(image)
        self.bullet_image = gfw.image.load(image)
        self.pattern = pattern
        # 적 이미지 프레임 인덱스 크기
        self.fidx = fidx

        self.image_destroy = gfw.image.load(image_destroy)
        self.delta = 0

        # 격추 이미지 프레임 인덱스 크기
        self.d_fidx = d_fidx
        self.shot_down = False
        
        # 현재 프레임 인덱스
        self.idx = 0

    def update(self):
        if self.shot_down = True:
            self.delta += gfw.delta_time
            self.idx = (int)(self.delta / (destroy_time / self.d_fidx))
            if self.delta > destroy_time:
                gfw.world.remove(self)

    def draw(self):
        if self.shot_down == True:
            x, y = self.pos
            x -= enemey_size[0] // 2
            y -= enemey_size[1] // 2
            Pos = x, y
            self.image_destroy.clip_draw_to_origin(self.idx * (self.image_destroy // self.d_fidx), 0, self.image_destroy // self.d_fidx, self.image_destroy.h, *Pos, *enemey_size)
        else:
            self.image.clip_draw_to_origin(self.fidx * (self.image // self.fidx), 0, self.image // self.fidx, self.image.h, *self.pos, *destroy_size)

    def destroy(self):
        self.idx = 0
        self.shot_down = True

class enemy_Boss:
    def __init__(self, image, bullet_image):
        self.image = gfw.image.load(image)
        self.bullet_image = gfw.image.load(image)
        self.pattern = 0
        self.bullet = []

    def update(self):
        pass

    def draw(self):
        for b in self.bullet:
            b.draw()

