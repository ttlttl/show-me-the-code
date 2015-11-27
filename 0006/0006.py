# -*- coding: utf-8 -*-
"""第 0006 题：你有一个目录，放了你一个月的日记，都是 txt,
   为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""
import os

def purify(text):
    word = text
    for r in ",.<>;:\"\'!@#%":
        word = word.replace(r, '')
    return word

def all_text_files(path, match):
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.split('.')[-1].lower() in match:
                yield os.path.join(parent, filename)

def top_n(words_list, n):
    new_list = [(v, k) for k, v in words_list.items()]
    new_list.sort(reverse=True)
    return new_list[0:n]

def top_n_of_file(file, n):
    statistics = {}
    with open(file, 'r') as f:
        text = f.read()
    words = [purify(w) for w in text.split()]
    for w in words:
        if w not in statistics.keys():
            statistics[w] = 1
        else:
            statistics[w] += 1
    top_n_list = top_n(statistics, n)
    return top_n_list

if __name__ == '__main__':
    n = 5
    text_files = all_text_files('.', ['txt'])
    for text_file in text_files:
        result = top_n_of_file(text_file, n)
        print('Top %d words of file %s are:' % (n, text_file))
        for num, word in result:
            print(word, num)