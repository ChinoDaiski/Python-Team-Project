import gfw
from pico2d import *
from gobj import *

class Background:
    def __init__(self, imageName, x, y, w, h, alpha):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.target = None
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.win_rect = x, h, self.w, self.h
        self.center = self.x + self.w // 2, self.y + self.h // 2
        self.alpha = alpha

        self.b = False

    def draw(self):
        gfw.image.setImageAlpha(self.image, self.alpha)
        self.image.clip_draw_to_origin(0, 0, self.image.w, self.image.h, self.x, self.y, self.w, self.h)

    def update(self):
        if self.b == False:
            #print(0, 0, self.image.w, self.image.h, *self.win_rect)
            self.b = True


class FixedBackground(Background):
    MARGIN_L, MARGIN_B, MARGIN_R, MARGIN_T = 20, 40, 20, 40
    def __init__(self, imageName):
        super().__init__(imageName)
        self.boundary = (
            FixedBackground.MARGIN_L, 
            FixedBackground.MARGIN_B,
            self.image.w - FixedBackground.MARGIN_R, 
            self.image.h - FixedBackground.MARGIN_T
        )
    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos
        sl = clamp(0, round(tx - self.cw / 2), self.image.w - self.cw)
        sb = clamp(0, round(ty - self.ch / 2), self.image.h - self.ch)
        self.win_rect = sl, sb, self.cw, self.ch

class InfiniteBackground(Background):
    def __init__(self, imageName, width=0, height=0):
        super().__init__(imageName)
        self.boundary = (-sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize)
        self.fix_x, self.fix_y = self.cw // 2, self.ch // 2
        if width == 0:
            width = self.image.w
        if height == 0:
            height = self.image.h
        self.w, self.h = width, height
    def set_fixed_pos(self, x, y):
        self.fix_x, self.fix_y = x, y
    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos

        # quadrant 3
        q3l = round(tx - self.fix_x) % self.image.w
        q3b = round(ty - self.fix_y) % self.image.h
        q3w = clamp(0, self.image.w - q3l, self.image.w)
        q3h = clamp(0, self.image.h - q3b, self.image.h)
        self.q3rect = q3l, q3b, q3w, q3h
        # quadrant 2
        self.q2rect = q3l, 0, q3w, self.ch - q3h
        self.q2origin = 0, q3h
        # quadrant 4
        self.q4rect = 0, q3b, self.cw - q3w, q3h
        self.q4origin = q3w, 0
        # quadrant 1
        self.q1rect = 0, 0, self.cw - q3w, self.ch - q3h
        self.q1origin = q3w, q3h

    def draw(self):
        self.image.clip_draw_to_origin(*self.q3rect, 0, 0)
        self.image.clip_draw_to_origin(*self.q2rect, *self.q2origin)
        self.image.clip_draw_to_origin(*self.q4rect, *self.q4origin)
        self.image.clip_draw_to_origin(*self.q1rect, *self.q1origin)

    def to_screen(self, point):
        x, y = point
        tx, ty = self.target.pos
        return self.fix_x + x - tx, self.fix_y + y - ty

    def translate(self, point):
        x, y = point
        tx, ty = self.target.pos
        dx, dy = x - self.fix_x, y - self.fix_y
        return tx + dx, ty + dy

class HorzScrollBackground:
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.scroll = 0
        self.speed = 0

    def update(self):
        self.scroll += self.speed * gfw.delta_time

    def set_scroll(self, scroll):
        self.scroll = scroll

    def draw(self):
        left, bottom = 0, 0
        page = self.image.w * self.ch // self.image.h
        curr = int(-self.scroll) % page
        if curr > 0:
            sw = int(1 + self.image.h * curr / self.ch)
            sl = self.image.w - sw
            src = sl, 0, sw, self.image.h
            dw = int(sw * self.ch / self.image.h)
            dst = curr - dw, 0, dw, self.ch
            self.image.clip_draw_to_origin(*src, *dst)
        dst_width = round(self.image.w * self.ch / self.image.h)
        while curr + dst_width < self.cw:
            dst = curr, 0, dst_width, self.ch
            self.image.draw_to_origin(*dst)
            curr += dst_width
        if curr < self.cw:
            dw = self.cw - curr
            sw = int(1 + self.image.h * dw / self.ch)
            src = 0, 0, sw, self.image.h
            dw = int(sw * self.ch / self.image.h)
            dst = curr, 0, dw, self.ch
            self.image.clip_draw_to_origin(*src, *dst)

    def to_screen(self, point):
        x, y = point
        return x - self.scroll, y

    def translate(self, point):
        x, y = point
        return x + self.scroll, y

    def get_boundary(self):
        return (-sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize)

    #     self.image.clip_draw_to_origin(*self.src_rect_1, *self.dst_rect_1)
    #     self.image.clip_draw_to_origin(*self.src_rect_2, *self.dst_rect_2)

    # private void drawHorizontal(Canvas canvas) {
    #     int left = 0;
    #     int top = 0;
    #     int right = UiBridge.metrics.size.x;
    #     int bottom = UiBridge.metrics.size.y;
    #     int pageSize = sbmp.getWidth() * (bottom - top) / sbmp.getHeight();

    #     canvas.save();
    #     canvas.clipRect(left, top, right, bottom);

    #     float curr = scrollX % pageSize;
    #     if (curr > 0) curr -= pageSize;
    #     curr += left;
    #     while (curr < right) {
    #         dstRect.set(curr, top, curr + pageSize, bottom);
    #         curr += pageSize;
    #         canvas.drawBitmap(sbmp.getBitmap(), srcRect, dstRect, null);
    #     }
    #     canvas.restore();
    # }
    
class VertScrollBackground:
    def __init__(self, imageName, cw, ch, alpha):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.cw, self.ch = cw, ch
        self.scroll = 0
        self.speed = 0
        self.alpha = alpha

    def update(self):
        self.scroll += self.speed * gfw.delta_time

    def set_scroll(self, scroll):
        self.scroll = scroll

    def draw(self):

        left, bottom = 0, 0
        page = self.image.h * self.cw // self.image.w
        curr = int(-self.scroll) % page
        if curr > 0:
            sh = int(1 + self.image.w * curr / self.cw)
            sb = self.image.h - sh
            src = 0, sb, self.image.w, sh
            dh = int(sh * self.cw / self.image.w)
            dst = 0, curr - dh, self.cw, dh
            
            gfw.image.setImageAlpha(self.image, self.alpha)
            self.image.clip_draw_to_origin(*src, *dst)
        dst_height = page #round(self.image.w * self.ch / self.image.h)
        while curr + dst_height < self.ch:
            dst = 0, curr, self.cw, dst_height

            gfw.image.setImageAlpha(self.image, self.alpha)
            self.image.draw_to_origin(*dst)
            curr += dst_height
        if curr < self.ch:
            dh = self.ch - curr
            sh = int(1 + self.image.w * dh / self.cw)
            src = 0, 0, self.image.w, sh
            dh = int(sh * self.cw / self.image.w)
            dst = 0, curr, self.cw, dh
            
            gfw.image.setImageAlpha(self.image, self.alpha)
            self.image.clip_draw_to_origin(*src, *dst)

    def to_screen(self, point):
        x, y = point
        return x - self.scroll, y

    def translate(self, point):
        x, y = point
        return x + self.scroll, y

    def get_boundary(self):
        return (-sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize)

image_gap = 1440 // 8

class VertexSolidScrollBackground:
    def __init__(self, imageName, x, y, cw, ch, standard_y, speed):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.x, self.y = x, y
        self.cw, self.ch = cw, ch
        self.start = standard_y
            
        self.speed = speed

        global px, py, alpha
        px = []
        py = []
        alpha = []

        global Num
        Num = 1440 // image_gap + 2
        for n in range(Num):
            px.append(n)
            py.append(n)
            alpha.append(n)

        
        for n in range(Num):
            if n % 3 == 0:
                px[n] = self.x + self.cw // 5
            elif n % 3 == 1:
                px[n] = self.x + self.cw // 5 * 2
            elif n % 3 == 2:
                px[n] = self.x + self.cw // 5 * 0
            py[n] = image_gap * (n - 1)
            #print(py[n])

        global image_h, image_w
        image_h = self.ch // 20 * 2
        image_w = self.cw // 20 * 3


        # # 첫 번째 이미지는 가운데에서 시작하여 내려간다. 1순위
        # px[0] = self.x + self.cw // 5
        # py[0] = image_gap * 2

        # # 두 번째 이미지는 오른쪽에서 시작하여 내려간다. 2순위
        # px[1] = self.x + self.cw // 5 * 2
        # py[1] = image_gap * 1

        # # 세 번째 이미지는 왼쪽에서 시작하여 내려간다. 3순위
        # px[2] = self.x + self.cw // 5 * 0
        # py[2] = image_gap * 0

        global dist        
        dist = self.start - self.y

    def update(self):

        for n in range(Num):
            # 이미지의 시작 y지점부터의 거리 계산
            py[n] += gfw.delta_time * self.speed
            if py[n] > self.ch + image_h:
                py[n] = 0

            # 이미지의 알파값 계산
            if py[n] >= dist // 3 * 2:
                alpha[n] = 255
            else:
                calculate_alpha = 255 / (dist // 3 * 2) * py[n]
                if calculate_alpha >= 255:
                    alpha[n] = 255
                alpha[n] = (int)(calculate_alpha)

    def draw(self):

        for n in range(Num):
            gfw.image.setImageAlpha(self.image, (int)(alpha[n]))
            self.image.clip_draw_to_origin(0, 0, self.image.w, self.image.h, px[n], self.start - py[n], image_w, image_h)
