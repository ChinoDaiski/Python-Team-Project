

# 적기에 대한 정보를 담고 있는 모듈

from pico2d import *
import gfw
import pattern
import function

# 적 이미지의 크기
enemey_size = 60, 60

# 적이 파괴되는 동안 걸리는 시간
DestroyTime = 1.0

# 파괴하는 이미지의 크기
destroy_size = 100, 100

# 데미지 이펙트 최대크기
max_damage_effect_size = 200, 200

# 데미지를 받는데 걸리는 시간
damage_time = 0.2

resource = 'res/'

MOVE_PPS = 5

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
    # 12. 체력
    # 13. MOVE_PPS
    def __init__(self, image, Mfidx, Mfidy, image_destroy, d_Mfidx, d_Mfidy, last_line_image_count, start_x, start_y, dst_x, dst_y, bullet_image, fire_pattern, move_pattern, speed, bullet_speed, hp, MOVE_PPS):
        self.startPos = start_x, start_y
        self.dstPos = dst_x, dst_y
        self.pos = self.startPos
        self.image = gfw.image.load(resource + image)
        self.bullet_image = gfw.image.load(resource + bullet_image)
        self.speed = speed
        self.bullet_speed = bullet_speed
        self.radius = enemey_size[0] // 2
        self.hp = hp
        self.MOVE_PPS = MOVE_PPS
        
        # 움직이는 방법과 탄을 발사하는 방법
        self.fire_pattern = fire_pattern
        self.move_pattern = move_pattern

        # 적 이미지 프레임 인덱스 크기
        self.image_destroy = gfw.image.load(resource + image_destroy)
        self.delta_time = 0
        self.move_delta_time = 0

        
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

        # 데미지를 받았을 때와 관련된 변수
        self.damage_effect_image = gfw.image.load(resource + 'damage_effect.png')
        self.get_damage = False
        self.damage_effect_delta_time = 0
        self.damage_effect_size = 0, 0
        self.bShotdown = False

        if enemey_size[0] >= enemey_size[1]:
            self.radius = enemey_size[0] // 2
        else:
            self.radius = enemey_size[1] // 2

        # 화면
        self.bb_left = -enemey_size[0] * 2
        self.bb_bottom = 0
        self.bb_right = get_canvas_width() // 7 * 5 + enemey_size[0] * 2
        self.bb_top = get_canvas_height() + enemey_size[0] * 2

        # 베지어 곡선 운동에 필요한 좌표
        mapX, mapY = gfw.world.getMapSize()

        self.bezier_pos = []
        for n in range(3):
            bezierPos = mapX, mapY // 4 * (n + 1)
            self.bezier_pos.append(bezierPos)

        self.t = 0

    def update(self):

        self.delta_time += gfw.delta_time
        self.move_delta_time += gfw.delta_time
        self.fidx = (int)((self.move_delta_time / 0.1) // 1 % 4 + 4) # 0 ~ 3

        # 움직이는 패턴에 따라 움직임

        # 움직이는 패턴 1 - 직선 운동(1차 베지어 곡선)
        if self.move_pattern == 1:
            x, y = self.pos
            px, py = self.dstPos
                
            dx = px - x
            dy = py - y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance == 0:
                return 0

            if dx == 0:
                dx = 0.0000001
            if dy == 0:
                dy = 0.0000001

            dx, dy = self.speed * dx / distance, self.speed * dy / distance
            
            x += dx * self.MOVE_PPS * gfw.delta_time
            y += dy * self.MOVE_PPS * gfw.delta_time
                
            self.pos = x, y

        # 움직이는 패턴 2 - 2차 베지어 곡선 운동
        elif self.move_pattern == 2:
            self.t += self.MOVE_PPS / 1000
            t = self.t
            x, y = (1 - t) ** 2 * self.startPos[0] + 2 * (1 - t) * t * self.bezier_pos[1][0] + t ** 2 * self.dstPos[0], (1 - t) ** 2 * self.startPos[1] + 2 * (1 - t) * t * self.bezier_pos[1][1] + t ** 2 * self.dstPos[1]
            self.pos = x, y

        # 움직이는 패턴 3 - 3차 베지어 곡선 운동
        elif self.move_pattern == 3:
            self.t += self.MOVE_PPS / 1000
            t = self.t
            x, y = (1 - t) ** 3 * self.startPos[0] + 3 * (1 - t) ** 2 * t * self.bezier_pos[0][0] + 3 * (1 - t) * t ** 2 * self.bezier_pos[2][0] + t ** 3 * self.dstPos[0], (1 - t) ** 3 * self.startPos[1] + 3 * (1 - t) ** 2 * t * self.bezier_pos[0][1] + 3 * (1 - t) * t ** 2 * self.bezier_pos[2][1] + t ** 3 * self.dstPos[1]
            self.pos = x, y

        # 탄 발사 패턴
        if self.delta_time > 1.0 and not self.bShotdown:
            if not self.bShoot:
                self.shoot()
                self.bShoot = True

        # 탄에 맞았을 경우 실행
        if self.get_damage:
            self.damage_effect_delta_time += gfw.delta_time
            self.damage_effect_size = (self.damage_effect_delta_time / damage_time) * max_damage_effect_size[0], (self.damage_effect_delta_time / damage_time) * max_damage_effect_size[1]
            if self.damage_effect_size[0] > max_damage_effect_size[0]:
                self.get_damage = False
                self.damage_effect_delta_time = 0
                self.damage_effect_size = 0, 0

        # 파괴될 경우 실행
        if self.bShotdown:
            self.enemy_delta_time += gfw.delta_time
            self.fidx, self.fidy = function.sprite_selector(self.d_Mfidx, self.d_Mfidy, self.last_line_image_count, DestroyTime, self.enemy_delta_time)
            if self.enemy_delta_time > DestroyTime:
                gfw.world.remove(self)

        if self.out_of_screen():
            gfw.world.remove(self)

    def draw(self):
        # 데미지를 받은 경우
        if self.get_damage:
            x, y = self.pos
            x -= self.damage_effect_size[0] // 2
            y -= self.damage_effect_size[1] // 2
            Pos = x, y
            gfw.image.setImageAlpha(self.damage_effect_image, 100)
            self.damage_effect_image.clip_draw_to_origin(0, 0, self.damage_effect_image.w, self.damage_effect_image.h, *Pos, *self.damage_effect_size)

        # 파괴될 경우
        if self.bShotdown:
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
        self.get_damage = True
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

    def setBezier(self, x, y):
        self.bezier_pos = x, y

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

