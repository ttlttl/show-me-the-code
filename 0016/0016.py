# -*- coding: utf-8 -*-
"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
"""
import xlwt
import json
from collections import OrderedDict

def read_txt(file):
    with open(file) as f:
        txt = f.read()
    return json.loads(txt, object_pairs_hook=OrderedDict)

def save_numbers_info(xls, info):
    file = xlwt.Workbook()
    table = file.add_sheet('numbers')
    line = 0
    for nums in info:
        column = 0
        for num in nums:
            table.write(line, column, num)
            column = column + 1
        line = line + 1
    file.save(xls)

def txt_to_xls(txt, xls):
    info = read_txt(txt)
    save_numbers_info(xls, info)

if __name__ == '__main__':
    txt_to_xls('numbers.txt', 'numbers.xls')