# -*- coding: utf-8 -*-
"""第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
import os
from PIL import Image

def all_images(path, match):
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.split('.')[-1].lower() in match:
                yield os.path.join(parent, filename)

def resize_img(input, size, output=None, zoom=False):
    print('Processing image file %s, given size %d*%d' % (input, size[0], size[1]))
    try:
        im = Image.open(input)
    except:
        print('Failed to load image file %s' % input)
    x, y = im.size
    print('Image original size: %d*%d' % (x, y))
    if zoom == True:
        newSize= size
    else:
        if x/y <= size[0]/size[1]:
            newSize = (int(size[1]*x/y), int(size[1]))
        else:
            newSize = (int(size[0]), int(size[0]*y/x))
    print('Image new size: %d*%d' % (newSize[0], newSize[1]))
    newIm = im.resize(newSize)
    im.close()
    path = os.path.dirname(input)
    baseName = os.path.basename(input)
    if output is None:
        newBaseName = 'New_' + baseName
    else:
        newBaseName = output
    newName = os.path.join(path, newBaseName)
    try:
        newIm.save(newName)
    except:
        print('Failed to save image file %s' % newName)


if __name__ == '__main__':
    size = (800,400)
    images = all_images('.', ['jpg', 'jpeg', 'png'])
    for image in images:
        resize_img(image,size)