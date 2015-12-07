# -*- coding: utf-8 -*-
"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""

def world_filter(word, filtered):
    if word in filtered:
        return "Human Rights"
    else:
        return "Freedom"

if __name__ == '__main__':
    with open('filtered_words.txt') as f:
        filtered = f.read().split('\n')
    while True:
        word = input('请输入(按ctrl+c结束):')
        result = world_filter(word, filtered)
        print(result)