# -*- coding: utf-8 -*-
"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def get_img_urls(page):
    soup = BeautifulSoup(page, "html.parser")
    imgs = soup.find_all('img', pic_type='0', class_='BDE_Image')
    return [img['src'] for img in imgs]

def get_tieba_img(url,img_dir='imgs', timeout=10):
    r = requests.get(url, timeout=timeout)
    if r.status_code != 200:
        print('Unable to load url %s' % url)
        return
    page = r.content.decode('utf-8')
    img_urls = get_img_urls(page)
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    for i,url in enumerate(img_urls):
        print('Saving img %d from %s' % (i, url))
        urlretrieve(url, os.path.join(img_dir,str(i)+'.'+ url.split('.')[-1]))
        print('Img %d Done!' % i)


if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/2166231880"
    urls = get_tieba_img(url)