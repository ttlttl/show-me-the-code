# -*- coding: utf-8 -*-
"""第 0009 题：一个HTML文件，找出里面的链接。
"""
import requests
from bs4 import BeautifulSoup

def get_html(url, code='utf-8', timeout=10):
    r = requests.get(url, timeout=timeout)
    content = r.content
    html = content.decode(code)
    return html

def get_all_links(html):
    soup = BeautifulSoup(html, "html.parser")
    all = soup.body.find_all('a')
    links = [a['href'] for a in all if a.has_attr('href') and 'http://' in a['href']]
    return links

if __name__ == '__main__':
    url = 'http://www.cnbeta.com/articles/453495.htm'
    html = get_html(url)
    links = get_all_links(html)
    for link in links:
        print(link)