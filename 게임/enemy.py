

# 적기에 대한 정보를 담고 있는 모듈

from pico2d import *
import gfw
import pattern
import function

# 적 이미지의 크기
enemey_size = 60, 60

# 적이 파괴되는 동안 걸리는 시간
DestroyTime = 0.3

# 파괴하는 이미지의 크기
destroy_size = 100, 100

resource = 'res/'

def init():
    pass


# 일반적인 적
# 자신의 이미지와 발사하는 탄의 이미지, 탄막의 종류가 다르다.
class enemy_Nomal:
    # 01. 자신의 이미지
    # 02. 이미지 최대 x, y프레임
    # 03. 파괴 이미지
    # 04. 파괴 이미지 최대 x, y프레임, 마지막 줄의 이미지 숫자
    # 05. 시작 위치
    # 06. 도착 위치
    # 07. 탄 이미지
    # 08. 탄을 발사하는 패턴 번호
    # 09. 움직이는 패턴 번호
    # 10. 스피드
    # 11. 탄의 스피드
    def __init__(self, image, Mfidx, Mfidy, image_destroy, d_Mfidx, d_Mfidy, last_line_image_count, start_x, start_y, dst_x, dst_y, bullet_image, fire_pattern, move_pattern, speed, bullet_speed, hp):
        self.pos = start_x, start_y
        self.dstPos = dst_x, dst_y
        self.image = gfw.image.load(resource + image)
        self.bullet_image = gfw.image.load(resource + bullet_image)
        self.speed = speed
        self.bullet_speed = bullet_speed
        self.radius = enemey_size[0] // 2
        self.hp = hp
        
        # 움직이는 방법과 탄을 발사하는 방법
        self.fire_pattern = fire_pattern
        self.move_pattern = move_pattern

        # 적 이미지 프레임 인덱스 크기
        self.image_destroy = gfw.image.load(resource + image_destroy)
        self.delta_time = 0
        self.move_delta_time = 0

        # 격추 이미지 프레임 인덱스 크기
        self.bShotdown = False
        
        # 현재 프레임 인덱스
        self.Mfidx = Mfidx
        self.Mfidy = Mfidy
        self.d_Mfidx = d_Mfidx
        self.d_Mfidy = d_Mfidy
        self.fidx = 0
        self.fidy = 0
        self.last_line_image_count = last_line_image_count

        self.enemy_delta_time = 0
        self.bShoot = False

        standard = 0
        if enemey_size[0] >= enemey_size[1]:
            self.radius = enemey_size[0] // 2
        else:
            self.radius = enemey_size[1] // 2
        standard = self.radius

        # 화면
        self.bb_left = -standard
        self.bb_bottom = -standard
        self.bb_right = get_canvas_width() // 7 * 5 + standard
        self.bb_top = get_canvas_height() + standard

    def update(self):
        self.delta_time += gfw.delta_time
        self.move_delta_time += gfw.delta_time
        self.fidx = (int)((self.move_delta_time / 0.1) // 1 % 4 + 4) # 0 ~ 3

        # 움직이는 패턴에 따라 움직임
        x, y = self.pos
        y -= self.speed * gfw.delta_time
        self.pos = x, y

        # 탄 발사 패턴
        if self.delta_time > 1.0:
            if not self.bShoot:
                self.shoot()
                self.bShoot = True

        # 탄에 맞았을 경우 실행
        if self.bShotdown == True:
            self.enemy_delta_time += gfw.delta_time
            self.fidx, self.fidy = function.sprite_selector(self.d_Mfidx, self.d_Mfidy, self.last_line_image_count, DestroyTime, self.enemy_delta_time)
            if self.enemy_delta_time > DestroyTime:
                gfw.world.remove(self)

        if self.out_of_screen():
            gfw.world.remove(self)

    def draw(self):
        # 탄에 맞았을 경우
        if self.bShotdown == True:
            x, y = self.pos
            x -= destroy_size[0] // 2
            y -= destroy_size[1] // 2
            Pos = x, y

            function.sprite_draw(self.image_destroy, self.d_Mfidx, self.d_Mfidy, self.fidx, self.fidy, *Pos, *destroy_size)
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
        patternName = 'enemyNormal_%d' % self.fire_pattern
        pattern.fire_pattern(patternName, self.bullet_image ,10, *self.pos, self.bullet_speed)

    def getDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.destroy()

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

class enemy_Boss:
    def __init__(self, image, bullet_image):
        self.image = gfw.image.load(image)
        self.bullet_image = gfw.image.load(image)
        self.fire_pattern = 0
        self.bullet = []

    def update(self):
        pass

    def draw(self):
        for b in self.bullet:
            b.draw()

