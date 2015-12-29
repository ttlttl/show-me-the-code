# -*- coding: utf-8 -*-
"""第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
from collections import Counter
import re

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        text = f.read()
    words = re.split(r'[;,.\s]\s*', text)
    counts = Counter(words)
    print(counts)
