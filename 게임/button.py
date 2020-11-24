
# 버튼 클래스
# 버튼의 이미지와 위치를 인자로 받아 해당 위치에 이미지를 그리고
# 마우스의 위치를 인자로 받아 위치에 따라 다른 이미지를 출력한다.
# 마우스 클릭시 위치에 따라 다른 이벤트를 넘긴다.


from pico2d import *
import gfw

MOVEMENT = 25
MAXIMUN = 60

class btn:

    # [ 이미지 이름, 이미지가 출력될 위치(좌하단), 이미지의 사이즈, 이미지 처리 이벤트, 처리시 넘길 스테이트 이름 ]을 인자로 받는다.
    def __init__(self, image, x, y, sx, sy, event, bSelect, state_name, bleft):
        # 버튼의 이미지
        self.Image = gfw.image.load(image)

        # 버튼이 출력될 지점의 시작점(좌하단)
        self.x = x
        self.y = y

        # 이벤트에 따라 움직일 버튼을 나타낸 숫자
        self.dx = 0

        # 출력될 버튼의 사이즈
        self.sx = sx
        self.sy = sy

        # 이벤트로 넘기는 스테이트 이름
        self.state_name = state_name

        # 자신이 선택됬는지 아닌지 확인하는 변수, 선택되면 true, 아니면 false
        self.bSelect = bSelect

        # 움직이는 버튼을 만들기 위한 값
        self.alpha = 0
        self.bleft = bleft
        self.bright = not bleft

    def draw(self):
        self.Image.clip_draw_to_origin(self.Image.w // 3 * self.dx, 0, self.Image.w // 3, self.Image.h, self.x + self.alpha, self.y, self.sx, self.sy)


    def update(self):
        if self.bSelect:
            self.dx = 1
        else:
            self.dx = 0

        if self.alpha > MAXIMUN:
            self.bright = False
            self.bleft = True
        elif self.alpha < -MAXIMUN:
            self.bright = True
            self.bleft = False


        if self.bleft:
            self.alpha -= gfw.delta_time * MOVEMENT

        elif self.bright:
            self.alpha += gfw.delta_time * MOVEMENT
        



    def handle_events(self, event):
        for e in event:
            if e.type == SDL_KEYDOWN:
                if e.type == SDLK_KP_ENTER:
                    if self.bSelect:
                        gfw.change(self.state_name)
                elif e.type == SDLK_UP or e.type == SDLK_DOWN:
                    if self.bSelect:
                        self.dx = 1
                    else:
                        self.dx = 0

    def quit(self):
        gfw.image.unload(self.Image)