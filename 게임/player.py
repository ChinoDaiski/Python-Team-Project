
# 플레이어 스테이트


from pico2d import *
import gfw
import background
import pattern
from generator import *
import function

resource = 'res/'

MOVE_PPS = 500
PLAYER_MOVEMENT = 0.4

PLAYER_SIZE = 80, 120
Bullet_Size = 24, 30
Bomb_Size = 80, 80

DestroyTime = 1.0

class Player:
    def __init__(self):

        # 플레이어 이미지 초기화
        global image
        image = gfw.image.load('res/sheet_player.png')

        # 플레이어 움직임 관련 초기화

        global delta_x, delta_y, pos
        x, y = gfw.world.getMapSize()
        pos = x // 2, 100
        delta_x, delta_y = 0, 0
        self.pos = pos

        # 플레이어의 이미지 출력을 위한 번호 (0 ~ 23)
        self.dx = 23 / 2

        # 플레이어 충돌 판정을 위한 반지름
        self.radius = (image.w // 24) // 2 // 2
        

        # 총을 발사하고 있는 중인지 아닌지 확인하는 변수
        global bFire
        bFire = False
        
        # 초당 나가는 탄알의 갯수를 조장하기 위한 레벨, 높을수록 많은 탄알이 나간다. 최대 4까지 조정 (0 ~ 4)
        global level
        level = 0

        global player_delta_time
        player_delta_time = 0

        # 플레이어의 라이프 갯수
        self.life = 3
        self.image_life = gfw.image.load(resource + 'life.png')

        self.bomb = 2
        self.image_bomb = gfw.image.load(resource + 'bomb.png')

        # 플레이어가 격추될 경우 사용하는 이미지
        self.image_shot_down = gfw.image.load(resource + 'bomb_player.png')
        self.fidx = 0
        self.fidy = 0
        self.Mfidx = 5
        self.Mfidy = 4
        self.last_line_image_count = 1
        self.bShotdown = False
        self.player_detroy_delta_time = 0

        self.bullet_sound = load_music(resource + 'sound_player_bullet.wav')
        self.bullet_sound.set_volume(1)

    def update(self):
        x, y = self.pos
    
        # 이번 프레임에 움직이는 양, delta_time으로 일괄적으로 조정
        x += delta_x * MOVE_PPS * gfw.delta_time
        y += delta_y * MOVE_PPS * gfw.delta_time

        #x = min(30, max(get_canvas_width() - 30, x))

        # 이미지의 가로 세로 길이를 받아온다.
        hw, hh = PLAYER_SIZE[0] // 2, PLAYER_SIZE[1] // 2
        map_size = gfw.world.getMapSize()

        x = clamp(hw, x, map_size[0] - hw)
        y = clamp(hh + PLAYER_SIZE[1] // 2, y, map_size[1] - hh)

        self.pos = x, y

        # 플레이어 이미지 관련 값 조절
        if delta_x == -1:
            if self.dx > 0:
                self.dx -= PLAYER_MOVEMENT

        elif delta_x == 0:
            if self.dx > 16:
                self.dx -= PLAYER_MOVEMENT

            elif self.dx < 8:
                self.dx += PLAYER_MOVEMENT

            elif self.dx >= 8 and self.dx < 16:
                self.dx += PLAYER_MOVEMENT

            if self.dx >= 15.5 and self.dx <= 16.5:
                self.dx = 8

        elif delta_x == 1:
            if self.dx < 23:
                self.dx += PLAYER_MOVEMENT

        if self.dx >= 23:
            self.dx = 19
        elif self.dx <= 0:
            self.dx = 4

        # 탄과 관련된 값 조절
        global bFire, level, player_delta_time
        if bFire:
            if player_delta_time > 1 / (12 + level * 3):
                self.fire()
                player_delta_time = 0

        # 플레이어의 델타타임
        player_delta_time += gfw.delta_time

        # 플레이어가 격추당했을 경우 실행되는 곳
        if self.bShotdown == True:
            self.player_detroy_delta_time += gfw.delta_time

            self.fidx, self.fidy = function.sprite_selector(self.Mfidx, self.Mfidy, self.last_line_image_count, DestroyTime, self.player_detroy_delta_time)

            if self.player_detroy_delta_time > DestroyTime:
                gfw.world.remove(self)
           

    def draw(self):
        if not self.bShotdown:
            # 플레이어 그리기
            x, y = self.pos
            x -= PLAYER_SIZE[0] // 2
            y -= PLAYER_SIZE[1] // 2
            Pos = x, y
            image.clip_draw_to_origin(image.w // 24 * (int)(self.dx), 0, image.w // 24, image.h, *Pos, *PLAYER_SIZE)

        else:
            # 폭탄 그리기
            x, y = self.pos
            x -= Bomb_Size[0] // 2
            y -= Bomb_Size[1] // 2
            Pos = x, y
            function.sprite_draw(self.image_shot_down, self.Mfidx, self.Mfidy, self.fidx, self.fidy, *Pos, *Bomb_Size)
           
    def handle_event(self, e):
        global delta_x, delta_y
        # =========
        # 이동 관련
        # =========
        # ==========================
        # 누를 경우
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                delta_x -= 1

            elif e.key == SDLK_RIGHT:
                delta_x += 1

            elif e.key == SDLK_UP:
                delta_y += 1
                
            elif e.key == SDLK_DOWN:
                delta_y -= 1

        # 눌렀다 땔 경우
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                delta_x += 1

            if e.key == SDLK_RIGHT:
                delta_x -= 1

            elif e.key == SDLK_UP:
                delta_y -= 1

            elif e.key == SDLK_DOWN:
                delta_y += 1
        # ==========================


        # =============
        # 탄막 발사 관련
        # =============
        # ==========================
        global bFire
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_z:
                bFire = True
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_z:
                bFire = False
        # ==========================

        #=================
        # 연습 관련
        #=================
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_x:
                self.destroy()

    def fire(self):
        x, y = self.pos
        y += (image.h // 2 + 20)
        pattern.fire_pattern('player', x, y)
        #generate_bullet('player', 'player', x, y)
        self.bullet_sound.set_volume(10)
        self.bullet_sound.play(1)
        

    def destroy(self):
        self.player_detroy_delta_time = 0
        self.bShotdown = True

