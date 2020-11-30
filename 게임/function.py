
import math
# 기타 기능 함수들 모음


# 인자로 이미지의 가로 숫자, 세로 숫자, 마지막 라인의 숫자, 이미지가 출력되는데 걸리는 시간, 기준이 되는 델타 타임을 받아서
# # 현재 이미지의 가로, 세로 번호를 return 하는 함수
def sprite_selector(Mfidx, Mfidy, last_line_image_count, total_time, standard_time):
    idx = (int)(standard_time / (total_time / (Mfidx * (Mfidy - last_line_image_count) + last_line_image_count)))
    fidx = idx // Mfidx
    fidy = idx - fidx * Mfidx
    return fidx, fidy


# 인자로 이미지, 프레임 최대 가로, 세로 숫자, 현재 프레임 가로, 세로 숫자, 그리기 시작하는 위치, 출력 크기를 받아서
# 그리는 함수
def sprite_draw(image, Mfidx, Mfidy, fidx, fidy, x, y, px, py):
    pos = x, y
    size = px, py
    image.clip_draw_to_origin(image.w // Mfidx * fidy, image.h // Mfidy * (Mfidy - fidx - 1), image.w // 5, image.h // 4, *pos, *size)

    
# 인자로 현재 위치(x, y)와 도착 위치(px, py)를 받아 두 점 사이의 각도를 반환하는 함수
def get_degree(x, y, px, py):
    dx = px - x
    dy = py - y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if distance == 0:
        return 0

    if dx == 0:
        dx = 0.0000001
    if dy == 0:
        dy = 0.0000001
    
    dx, dy = dx / distance, dy / distance
    angle = math.atan2(dy, dx) / math.pi * 180
    
    return angle