# -*- coding: utf-8 -*-
"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样,
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

def world_filter(word, filtered):
    for fil in filtered:
        if fil in word:
            word = word.replace(fil, ''.join(['*' for i in range(len(fil))]))
    return word

if __name__ == '__main__':
    with open('filtered_words.txt') as f:
        filtered = f.read().split('\n')
    while True:
        word = input('请输入(按ctrl+c结束):')
        result = world_filter(word, filtered)
        print(result)