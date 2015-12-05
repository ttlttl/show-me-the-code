# -*- coding: utf-8 -*-
"""
第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
参考：http://blog.csdn.net/cdnight/article/details/49636893
"""
from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random

class VerifyImage():
    """
    Simple Usage:

    v = VerifyImage()
    optional:
        v.set_str_num(n) 4,5...
        v.set_lines(min, max)
        v.set_point_chance(n)
    v.create()
    str = v.str
    img = v.img
    img.save('%s.jpg' % str, 'JPEG')
    """
    def __init__(self):
        self._mode = 'RGB'
        self._size = (120, 30)
        self._img_type = 'jpg'
        self._font_type = 'arial.ttf'
        self._font_size = 18
        self._bg_color = (255, 255, 255)
        self._n_strs = 4
        self._n_lines = (1,3)
        self._point_chance = 6
        self._draw_lines = True
        self._draw_points = True
        self._fg_color = self._rand_color()
        self.str = None
        self.img = None

    def set_lines(self, min, max):
        self._n_lines = (min, max)

    def set_point_chance(self, n):
        self._point_chance = n

    def set_str_num(self, n):
        self._n_strs = n

    def _rand_text(self):
        digest = '234578'
        lettr = 'cdefhkmnprstxy'
        keys = digest+lettr+lettr.upper()
        return ''.join(random.sample(keys, self._n_strs))

    def _rand_color(self):
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        return r, g, b

    def create(self):
        self.str = self._rand_text()
        x,y = self._size
        img = Image.new(self._mode, self._size, self._bg_color)
        draw = ImageDraw.Draw(img)

        def _draw_line():
            line_num = random.randint(*self._n_lines)
            for i in range(line_num):
                begin = (random.randint(0, self._size[0]), random.randint(0, self._size[1]))
                end = (random.randint(0, self._size[0]), random.randint(0, self._size[1]))
                draw.line([begin, end], fill=(0, 0, 0))

        def _draw_points():
            chance = min(100, max(0, int(self._point_chance)))
            for w in range(x):
                for h in range(y):
                    tmp = random.randint(0, 100)
                    if tmp > 100 - chance:
                        draw.point((w, h), fill=(0, 0, 0))

        def _draw_str():
            font = ImageFont.truetype(self._font_type, self._font_size)
            font_x, font_y = font.getsize(self.str)
            pos_x = (x - font_x) / 3
            pos_y = (y - font_y) / 3
            for c in self.str:
                draw.text((pos_x, pos_y),
                        c, font=font, fill=self._rand_color())
                pos_x = pos_x + (x - font_x) / 6

        if self._draw_lines:
            _draw_line()
        if self._draw_points:
            _draw_points()
        _draw_str()

        params = [1 - float(random.randint(1, 2)) / 100,
                  0,
                  0,
                  0,
                  1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500,
                  0.001,
                  float(random.randint(1, 2)) / 500
                  ]
        img = img.transform(self._size, Image.PERSPECTIVE, params)
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

        self.img = img

if __name__ == '__main__':
    v = VerifyImage()
    for i in range(20):
        v.create()
        v.img.save('%s.jpg' % v.str,'JPEG')
