
# 총알 클래스

# 자신의 이미지와 위치, 반지름, 속도, 움직이는 방향을 가지고 있다.
# 해당 총알은 맵 밖을 벗어나면 삭제된다.


from pico2d import *
import gfw
import function
from math import *

MOVE_PPS = 200
Bullet_Size = 24, 30
RESOURCE = 'res/'


# 인자로
#==========================
# 탄 이미지
# 탄의 위치(x, y)
# 탄의 크기(size_x, size_y)
# 스피드
# 이동 방향(각도)
# 탄의 알파값
#==========================
#을 받는다.
class Bullet:
    def __init__(self, image, x, y, size_x, size_y, speed, direction, alpha):
        # 총알의 이미지, 위치, 탄의 크기, 스피드, 이동 방향를 인자로 받음
        self.startPos = x, y
        self.image = image
        self.pos = self.startPos
        self.size = size_x, size_y
        self.speed = speed
        self.direction = direction # 이동 방향은 각도를 의미한다.
        
        # 충돌 처리를 위한 반지름
        self.radius = 0
        standard = 0
        if size_x >= size_y:
            self.radius = size_y // 2
            standard = size_x
        else:
            self.radius = size_x // 2
            standard = size_y

        
        # 화면 밖을 나가면 소멸
        self.bb_left = -standard
        self.bb_bottom = -standard
        self.bb_right = get_canvas_width() // 7 * 5 + standard
        self.bb_top = get_canvas_height() + standard

        self.alpha = alpha
        self.angle = 0

        self.target_object = []

        # 베지어 곡선 처리를 위한 값 설정
        self.bezier_pos = 0, 0
        self.t = 0.0
        self.delta_time = 0

    def set_target(self, Object):
        if Object in gfw.world.objects_at(gfw.layer.enemy):
            self.target_object = Object

    def set_Bezier(self, x, y):
        self.bezier_pos = x, y


    def update(self):

        global x, y, dx, dy
        self.delta_time += gfw.delta_time
        # if self.delta_time 

        # 자동 추적 기능
        if self.target_object in gfw.world.objects_at(gfw.layer.enemy):
            x, y = self.pos
            px, py = self.target_object.pos
            
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
            degree = function.get_degree(px, py, x, y)
            self.angle = (degree + 90) * math.pi / 180


            self.t += MOVE_PPS / 1000 / 10
            t = self.t
            x, y = (1 - t) ** 2 * self.startPos[0] + 2 * (1 - t) * t * self.bezier_pos[0] + t ** 2 * self.target_object.pos[0], (1 - t) ** 2 * self.startPos[1] + 2 * (1 - t) * t * self.bezier_pos[1] + t ** 2 * self.target_object.pos[1]
            self.pos = x, y

        # 일반적인 경우
        else:
            x, y = self.pos
            dx, dy = self.speed * cos(self.direction * pi / 180), self.speed * sin(self.direction * pi / 180)
            self.angle = -math.atan2(dx, dy)

            x += dx * MOVE_PPS * gfw.delta_time
            y += dy * MOVE_PPS * gfw.delta_time
            self.pos = x, y

        if self.out_of_screen():
            gfw.world.remove(self)
            

    def draw(self):

        SDL_SetTextureBlendMode(self.image.texture, SDL_BLENDMODE_BLEND)
        SDL_SetTextureAlphaMod(self.image.texture, self.alpha)
        x, y = self.pos
        x -= self.size[0] // 2
        y -= self.size[1] // 2
        Pos = x, y
        self.image.composite_draw(self.angle, '', *Pos, *self.size)
        #self.image.clip_draw_to_origin(0, 0, self.image.w, self.image.h, *Pos, *Bullet_Size)


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