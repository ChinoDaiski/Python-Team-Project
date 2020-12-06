
# 게임 스테이지 1번 state

from pico2d import *
import gfw
import background
import player
import generator
import enemy
import collision
import pattern
from score import Score
import stage_gen

import pyautogui

resource = 'res/'

# 점수를 출력하기 위한 폰트의 색상
SCORE_TEXT_COLOR = (255, 255, 255)



score_start_y = 1340
score_gap = 100



def enter():
    global MAP_SIZE
    MAP_SIZE = get_canvas_width() // 7 * 5, get_canvas_height()
    
    gfw.world.initMapSize(*MAP_SIZE)

    # 월드에 bg, ui 추가
    # bg = 뒤에 나오는 갈색 화면
    # bg_game = 게임 화면
    # player = 플레이어 화면
    # ui = ui 관련 화면
    gfw.world.init(['bg', 'bg_game', 'player', 'bullet', 'enemy', 'enemy_bullet', 'special_enemy_bullet', 'ui'])

    # bg 설정
    global bg
    #bg = background.Background('bg_stage.png', 0, 0, get_canvas_width(), get_canvas_height(), 255)
    #gfw.world.add(gfw.layer.bg, bg)

    bg = background.Background('bg_stage.PNG', MAP_SIZE[0], 0, get_canvas_width() - MAP_SIZE[0], MAP_SIZE[1], 255)
    gfw.world.add(gfw.layer.ui, bg)
    bg = background.Background('bg_stage_right.PNG', MAP_SIZE[0], 0, get_canvas_width() - MAP_SIZE[0], MAP_SIZE[1], 50)
    gfw.world.add(gfw.layer.ui, bg)
    bg = background.Background('reimu03.PNG', MAP_SIZE[0], 100, get_canvas_width() - MAP_SIZE[0], MAP_SIZE[1] // 2, 255)
    gfw.world.add(gfw.layer.ui, bg)

    bg = background.VertScrollBackground('bg_stage_03.png', MAP_SIZE[0], MAP_SIZE[1], 255)
    bg.speed = 800
    gfw.world.add(gfw.layer.bg, bg)

    #image_left, image_right, x, y, cw, ch, standard_y, speed_down, speed_sideway01, speed_sideway02, speed_sideway03
    #bg2 = background.VertexSolidScrollBackground('tree_02.png', 0, 0, 1825, 1440, 1440, 200)
    #gfw.world.add(gfw.layer.bg_game, bg2)

    bg = background.VertScrollBackground('clouds.png', 1825, 2000, 150)
    bg.speed = 40
    #gfw.world.add(gfw.layer.bg, bg)

    # 플레이어 초기화
    global player
    player = player.Player()
    player.level = 2
    player.bullet_speed = 8
    gfw.world.add(gfw.layer.player, player)

    # 탄 관련 초기화
    generator.init()
  
    # 점수판 관련 초기화
    global gap_w, gap_h
    gap_w = MAP_SIZE[0] // 10
    gap_h = MAP_SIZE[1] // 15

    global score, Hiscore
    score = Score(MAP_SIZE[0] + gap_w * 2, MAP_SIZE[1] - gap_h * 2)
    Hiscore = Score(MAP_SIZE[0] + gap_w * 2, MAP_SIZE[1] - gap_h)
    gfw.world.add(gfw.layer.ui, score)
    gfw.world.add(gfw.layer.ui, Hiscore)
    Hiscore.score = 1

    # 폰트 관련 초기화
    global font, font_size
    font_size = MAP_SIZE[0] // 50
    font = gfw.font.load(resource + 'ConsolaMalgun.ttf', font_size)

    # 배경음악 관련 초기화
    global bg_music
    bg_music = load_wav(resource + 'stage01_background.wav')
    bg_music.set_volume(50)
    bg_music.play(1)

    # 적 관련 초기화
    global emy
    x = MAP_SIZE[0] // 2
    y = MAP_SIZE[1]
    
    stage_gen.init()
    # 적 임시 생성
    # for n in range(10):
    #     emy = enemy.enemy_Nomal('enemy01.png', 12, 1, 'enemy01_bomb.png', 5, 5, 1, x // 100 * n, y, 0, 0, 'enemy01_bullet.png', 4, 0, 100, 3, 10)
    #     gfw.world.add(gfw.layer.enemy, emy)

def update():

    gfw.world.update()
    generator.update()
    stage_gen.update()

    # if not gfw.world.count_at(gfw.layer.enemy) == 0:
    #     for n in gfw.world.objects_at(gfw.layer.enemy):
    #         print(n)

    collision.check_collision()
    score.update()


    #print(gfw.world.count_at(gfw.layer.enemy))
    
    pattern.update()

def draw():

    gfw.world.draw()

   # 폰트 출력 부분
    global gap_w, gap_h
    score_start_y = MAP_SIZE[1] - gap_h
    gap = gap_w // 4

    # 최고 점수
    font.draw(MAP_SIZE[0] + gap, score_start_y, 'Hiscore', SCORE_TEXT_COLOR)

    # 현재 점수
    font.draw(MAP_SIZE[0] + gap, score_start_y - gap_h, 'Score', SCORE_TEXT_COLOR)
    # 플레이어의 생명
    font.draw(MAP_SIZE[0] + gap, score_start_y - gap_h * 2, 'Player', SCORE_TEXT_COLOR)
    for n in range(player.life):
        player.image_life.clip_draw(0, 0, player.image_life.w, player.image_life.h, MAP_SIZE[0] + round(gap_w * 1.5) + n * 60, score_start_y - gap_h * 2, 40, 40)

    # 폭탄의 갯수
    font.draw(MAP_SIZE[0] + gap, score_start_y - gap_h * 3, 'Bomb', SCORE_TEXT_COLOR)
    for n in range(player.bomb):
        player.image_bomb.clip_draw(0, 0, player.image_life.w, player.image_life.h, MAP_SIZE[0] + round(gap_w * 1.5) + n * 60, score_start_y - gap_h * 3, 40, 40)

    # 파워 게이지
    font.draw(MAP_SIZE[0] + gap, score_start_y - gap_h * 4, 'Power', SCORE_TEXT_COLOR)
    # 보호막 갯수
    font.draw(MAP_SIZE[0] + gap, score_start_y - gap_h * 5, 'Graze', SCORE_TEXT_COLOR)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

    global player
    player.handle_event(e)

def exit():
    pass


def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()

