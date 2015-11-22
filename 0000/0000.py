# -*- coding: utf-8 -*-
"""第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
参考：http://pillow.readthedocs.org/en/latest/reference/ImageDraw.html
      http://pillow.readthedocs.org/en/latest/reference/ImageFont.html
"""

from PIL import Image, ImageFont, ImageDraw

fontFile = 'C:\Windows\Fonts\Calibri.ttf'
inputFileName = 'input.jpg'
outputFileName = 'output.jpg'

def make_font(fontFile, size):
    font = ImageFont.truetype(fontFile, size)
    return font

# xy, per
def draw_text(input, output, text, pers, font, color):
    try:
        im = Image.open(input)
    except:
        print('Failed to load image file %s' % inputFileName)

    x, y = im.size
    draw = ImageDraw.Draw(im)
    draw.text((x*pers[0]/100, y*pers[1]/100), text, color, font)
    im.save(output)

if __name__ == '__main__':
    font = make_font(fontFile, 60)
    draw_text(inputFileName, outputFileName, '99+', (80, 10), font, 'red')
