# -*- coding: utf-8 -*-
"""第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
   包括空行和注释，但是要分别列出来。
"""
import os

def all_text_files(path, match):
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.split('.')[-1].lower() in match:
                yield os.path.join(parent, filename)

def statistics(file):
    all = 0
    comments = 0
    empty = 0
    comments_start = False
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            all = all + 1
            line = line.lstrip(' ')
            # Comments lines start with ''' or """
            if comments_start:
                comments = comments + 1
                if line.startswith('"""') or line.startswith("'''"):
                    comments_start = False
                    continue
            if line.startswith('"""') or line.startswith("'''") and not comments_start:
                comments = comments + 1
                comments_start = True

            # Comment line start with #
            if line.startswith('#'):
                comments = comments +1

            # Empty line
            if line.startswith('\n'):
                empty = empty + 1

        return all, comments, empty

def statistics_all_files(path, match):
    all = 0
    comments = 0
    empty = 0
    files = all_text_files(path, match)
    for file in files:
        a, c, e = statistics(file)
        all = all + a
        comments = comments + c
        empty = empty + e
    return all, comments, empty

if __name__ == '__main__':
    all, comments, empty = statistics_all_files('..', 'py')
    print('Got %d lines, comments %d line, empty %d line, code %d line' %
          (all, comments, empty, all-comments-empty))