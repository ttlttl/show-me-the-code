# -*- coding: utf-8 -*-
"""第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
import os
from PIL import Image

def img_name_iterator(path, match):
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.split('.')[-1].lower() in match:
                yield os.path.join(parent, filename)

def resize_img(input,size, output=None, zoom=True):
    try:
        im = Image.open(input)
    except:
        print('Failed to load image file %s' % input)
    x, y = (100,40)
    if zoom == True:
        newSize= size
    else:
        if x/y <= size[0]/size[1]:
            newSize = (int(size[1]*x/y), int(size[1]))
        else:
            newSize = (int(size[0]), int(size[0]*y/x))
    newIm = im.resize(newSize)
    path = os.path.dirname(input)
    baseName = os.path.basename(input)
    if output is None:
        newBaseName = 'New_' + baseName
    else:
        newBaseName = output
    newName = os.path.join(path, newBaseName)
    newIm.save(newName)


if __name__ == '__main__':
    iter = img_name_iterator('.', ['jpg', 'jpeg', 'png'])
    for i in iter:
        resize_img(i,(1000,500), zoom=False)