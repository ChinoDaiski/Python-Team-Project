from pico2d import *
from helper import *

RESOURCE_DIRECTORY = 'image/'

Height = 600
Width = 800

global events
global running

class Grass:
    def __init__(self):
        self.pos = 400, 30
        self.image = load_image(RESOURCE_DIRECTORY + 'grass.png')

    def draw(self):
        self.image.draw(self.pos[0], self.pos[1])

    def update(self):
        pass


class Character:
    def __init__(self):
        self.pos = 20, 85   # 현재 위치
        self.speed = 5      # 스피드
        self.delta = 0, 0   # 움직이는 정도
        self.target = self.pos  # 도착 지점
        self.frame = 0      # 애니메이션 작업을 위한 프레임
        self.image = load_image(RESOURCE_DIRECTORY + 'run_animation.png')
        self.done = True    # 움직임을 표현하는 bool형 변수 True면 움직이지 않고, False면 움직인다.

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.pos[0], self.pos[1])

    def update(self):
        self.frame = (self.frame + 1) % 8

        # 움직이는 것이 끝나지 않았으면
        if not self.done:
            # 현재 위치가 도착 지점과 같다면
            if self.pos == self.target:
                # 움직임을 멈춘다.
                self.done = True

            # 현재 위치가 도착 지점과 같지 않다면
            elif self.pos != self.target:
                # x, y 이동 거리를 구하여 delta 에 넣고
                self.delta = delta(self.pos, self.target, self.speed)
                # 현재 위치와 움직임이 끝났는지에 대한 여부를 최신화 한다.
                self.pos, self.done = move_toward(self.pos, self.delta, self.target)



def handle_events():
    global events
    global running

    events = get_events()
    for event in events:
        # 우상단 X 버튼을 누를 경우
        if event.type == SDL_QUIT:
            running = False

        # esc 버튼을 누를 경우
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        # 마우스를 눌렀을 경우
        elif event.type == SDL_MOUSEBUTTONDOWN:
            # 캐릭터가 움직이지 않을 경우
            if character.done:
                character.target = event.x, Height - event.y - 1
                # 캐릭터를 움직이게 함
                character.done = False


# -------------------------------------------------------------------------------------
open_canvas(Width, Height)

character = Character()
grass = Grass()

objects = character, grass

running = True
while running:
    clear_canvas()

    for obj in objects:
        obj.draw()

    for obj in objects:
        obj.update()


    update_canvas()
    handle_events()
    delay(0.04)

close_canvas()