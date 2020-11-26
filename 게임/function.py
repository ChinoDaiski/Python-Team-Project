

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