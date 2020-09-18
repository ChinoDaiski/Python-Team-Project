from pico2d import *

def handle_events():
    global running      # while문을 돌아가게 하는 변수
    global x            # 캐릭터의 x좌표값
    global y            # 캐릭터의 y좌표값
    global dx           # 캐릭터의 움직이는 방향을 나타내는 변수
                        # -1 -> 왼쪽    1 -> 오른쪽



                        
    events = get_events()
    for i in events:
        print(e.type)
      	        # 키를 눌렀으면 다른 키들이 출력된다.
        if e.type == SDL_QUIT:
            running = False;
        #=================================================================
        elif e.type == SDL_KEYDOWN:	# 키를 눌렀을 경우
            if e.key == SDLK_ESCAPE:
                print("종료키 출력!")
                running = False
            elif e.key == SDL_LEFT:
                dx-=1
            elif e.key == SDL_RIGHT:
                dx+=1
        #=================================================================
        elif e.type == SDL_KEYUP:
            if e.key == SDL_LEFT:   # 키를 누르고 있다가 뺄 경우 움직임을 멈춘다.
                dx+=1
            elif e.key == SDL_RIGHT:
                dx-=1
        #=================================================================
        elif e.type == SDL_MOUSEMOTION:
            x = e.x         # 마우스가 있는 좌표에 캐릭터가 생성된다.
            y = get_canvas_height() - e.y - 1
                            # window 좌표계는 좌상단이 0 ~ 600 이지만
                            # pico2d에서의 좌표계는 좌하단이 0 ~ 599 이다.
                            # 1픽셀 차이가 있기 때문에 마지막에 1을 빼서 픽셀단위를 맞춰준다.



                

open_canvas()           # 여기 x, y 좌표를 넣으면 열리는 캔버스의 크기가 달라진다.

grass = load_image('..\\파이참\\image\\grass.png')
character = load_image('..\\파이참\\image\\run_animation.png')


dx=0
frame = 0


x,y = get_canvas_width()

hide_cursor() # 마우스 커서를 없애는 함수 이 함수를 사용하면 캔버스 내부에선 마우스 커서가 보이지 않는다.
 
running = True
while running:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,90)
    update_canvas()
    handle_events()

    x+=dx
    
    frame=(frame+1)%8
    # x+=5
    delay(0.03)

close_canvas()

















