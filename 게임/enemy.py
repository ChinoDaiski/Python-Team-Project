

# 적기에 대한 정보를 담고 있는 모듈

from pico2d import *
import gfw
import pattern
import function

# 적 이미지의 크기
enemey_size = 40, 40

# 적이 파괴되는 동안 걸리는 시간
DestroyTime = 0.3

# 파괴하는 이미지의 크기
destroy_size = 80, 80

resource = 'res/'

def init():
    pass


# 일반적인 적
# 자신의 이미지와 발사하는 탄의 이미지, 탄막의 종류가 다르다.
class enemy_Nomal:
    def __init__(self, image, fidx, image_destroy, d_fidx, x, y, bullet_image, pattern, speed):
        self.pos = x, y
        self.image = gfw.image.load(resource + image)
        self.bullet_image = gfw.image.load(resource + bullet_image)
        self.pattern = pattern
        self.speed = speed
        self.radius = enemey_size[0] // 2
        # 적 이미지 프레임 인덱스 크기
        self.image_destroy = gfw.image.load(resource + image_destroy)
        self.delta_time = 0

        # 격추 이미지 프레임 인덱스 크기
        self.d_fidx = d_fidx
        self.bShotdown = False
        
        # 현재 프레임 인덱스
        self.Mfidx = 0
        self.Mfidy = 0
        self.fidx = 0
        self.fidy = 0
        self.last_line_image_count = 1

        self.enemy_delta_time = 0
        self.bShoot = False

    def update(self):
        self.delta_time += gfw.delta_time

        # 움직이는 패턴
        x, y = self.pos
        y -= self.speed * gfw.delta_time
        self.pos = x, y
        
        if self.delta_time > 1.0:
            if not self.bShoot:
                self.shoot()
                self.bShoot = True

        # 탄에 맞았을 경우 실행
        if self.bShotdown == True:

            self.enemy_delta_time += gfw.delta_time
            self.fidx, self.fidy = function.sprite_selector(self.Mfidx, self.Mfidy, self.last_line_image_count, DestroyTime, self.enemy_delta_time)
            if self.enemy_delta_time > DestroyTime:
                gfw.world.remove(self)

    def draw(self):
        # 탄에 맞았을 경우
        if self.bShotdown == True:
            x, y = self.pos
            x -= destroy_size[0] // 2
            y -= destroy_size[1] // 2
            Pos = x, y

            self.Mfidx = 5
            self.Mfidy = 5

            function.sprite_draw(self.image_destroy, self.Mfidx, self.Mfidy, self.fidx, self.fidy, *Pos, *destroy_size)
            #self.image_destroy.clip_draw_to_origin(self.idx * (self.image_destroy.w // self.d_fidx), 0, self.image_destroy.w // self.d_fidx, self.image_destroy.h, *Pos, *enemey_size)

        # 아닐 경우
        else:
            self.Mfidx = 12
            x, y = self.pos
            x -= enemey_size[0] // 2
            y -= enemey_size[1] // 2
            Pos = x, y
            self.image.clip_draw_to_origin(self.fidx * (self.image.w // self.Mfidx), 0, self.image.w // self.Mfidx, self.image.h, *Pos, *enemey_size)

    def destroy(self):
        self.idx = 0
        self.bShotdown = True

    def shoot(self):
        patternName = 'enemy%d' % self.pattern
        pattern.fire_pattern(patternName, *self.pos)


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

