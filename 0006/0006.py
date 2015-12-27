# -*- coding: utf-8 -*-
"""第 0006 题：你有一个目录，放了你一个月的日记，都是 txt,
   为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""
import os
from collections import Counter

def purify(text):
    word = text
    for r in ",.<>;:\"\'!@#%":
        word = word.replace(r, '')
    return word

def files(path, match):
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.split('.')[-1].lower() in match:
                yield os.path.join(parent, filename)

def statistics(words, n):
    return Counter(words).most_common(n)

if __name__ == '__main__':
    n = 5
    for file in files('.', ['txt']):
        with open(file) as f:
            words = [purify(w) for w in f.read().split()]
            print('Top %d words of file %s are:' % (n, file))
            print(Counter(words).most_common(n))
