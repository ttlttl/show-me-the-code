# -*- coding: utf-8 -*-
"""第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
from collections import Counter

def purify(text):
    word = text
    for r in ",.<>;:\"\'!@#%":
        word = word.replace(r, '')
    return word

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        text = f.read()
    words = [purify(w) for w in text.split()]
    counts = Counter(words)
    print(counts)
