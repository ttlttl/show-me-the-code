# -*- coding: utf-8 -*-
"""第 0008 题：一个HTML文件，找出里面的正文。
"""
import requests
from bs4 import BeautifulSoup

def get_html(url, code='utf-8', timeout=10):
    r = requests.get(url, timeout=timeout)
    content = r.content
    html = content.decode(code)
    return html

def get_cnbeta_content(html):
    soup = BeautifulSoup(html, "html.parser")
    c = soup.body.find_all('section', class_='article_content')[0]
    ps = c.find_all('p')
    content = [p.string for p in ps if not p.has_attr('class')]
    content = [r for r in content if r]
    return content

def get_content(url, code='utf-8', timeout=10):
    html = get_html(url, code=code, timeout=timeout)
    content = get_cnbeta_content(html)
    return content

if __name__ == '__main__':
    url = 'http://www.cnbeta.com/articles/453495.htm'
    content = get_content(url)
    for p in content:
        print(p)