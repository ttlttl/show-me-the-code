# -*- coding: utf-8 -*-
"""第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

def purify(text):
    word = text
    for r in ",.<>;:\"\'!@#%":
        word = word.replace(r, '')
    return word


with open('test.txt', 'r') as f:
    text = f.read()
words = [purify(w) for w in text.split()]
statistics = {}
for w in words:
    if w not in statistics.keys():
        statistics[w] = 1
    else:
        statistics[w] += 1

for k, v in statistics.items():
    print(k,v)
