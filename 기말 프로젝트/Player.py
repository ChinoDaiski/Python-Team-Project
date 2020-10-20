
from gfw import *
from pico2d import *
import gfw.gfw_image



canvas_width = 600
canvas_height = 800
resource = 'resource/'


class Player:

    image = None


    def __init__(self):
        # 가져오는 전역 변수
        global resource
        global canvas_width
        global canvas_height

        # 플레이어 위치
        self.x = canvas_width//2
        self.y = canvas_height//5

        # 플레이어 이동 가속도
        self.dx = 0
        self.dy = 0
        
        # 플레이어 이미지
        if Player.image == None:
            Player.image = gfw.gfw_image.load(resource + 'hakurei_reimu/reimu_left_right.png')

        # 플레이어 이미지 프레임
        self.fidx = 0
        self.fidy = 0
        
        # 플레이어 이미지 가로 및 세로 크기
        self.imageWidth = 25
        self.imageHeight = 34


    def update(self):

        # 움직임 관련

        # 좌우 이동
        if (self.x >= (self.imageWidth//2)) and (self.x <= canvas_width - self.imageWidth//2):
            self.x += self.dx
        elif (self.x <= self.imageWidth//2):
            self.x+=1
        elif (self.x >= canvas_width - self.imageWidth//2):
            self.x-=1

        # 상하 이동
        if (self.y >= self.imageHeight//2) and (self.y <= canvas_height - self.imageHeight//2):
            self.y += self.dy
        elif (self.y <= self.imageHeight//2):
            self.y+=1
        elif (self.y >= canvas_height - self.imageHeight//2):
            self.y-=1

        self.fidx = (self.fidx + 1) % 4
        self.fidy = 4

        # 공격


    def late_update(self):
        pass
        

    def draw(self):
        self.image.clip_draw(self.imageWidth * self.fidx, self.imageHeight * self.fidy, 25, 34, self.x, self.y)
        

    def handle_event(self, e):
        # 키를 누른 경우
        if e.type == SDL_KEYDOWN:

            if e.key == SDLK_LEFT:
                self.dx -=1
            elif e.key == SDLK_RIGHT:
                self.dx +=1
            elif e.key == SDLK_UP:
                self.dy +=1
            elif e.key == SDLK_DOWN:
                self.dy -=1

            # 키를 땔 경우
        if e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx +=1
            elif e.key == SDLK_RIGHT:
                self.dx -=1
            elif e.key == SDLK_UP:
                self.dy -=1
            elif e.key == SDLK_DOWN:
                self.dy +=1         

           






if __name__ == "__main__":
	print("Running test code ^_^")
