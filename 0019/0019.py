# -*- coding: utf-8 -*-
"""
第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!--
    数字信息
-->

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]

</numbers>
</root>
"""
import xlrd
import json
from xml.dom import minidom

def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    return [list(map(int,table.row_values(i))) for i in range(table.nrows)]

def write_xml(filename, data):
    doc = minidom.Document()
    node_root = doc.createElement('root')
    node_numbers = doc.createElement('numbers')
    node_comment = doc.createComment('数字信息\n')
    node_numbers.appendChild(doc.createTextNode(data))
    node_root.appendChild(node_comment)
    node_root.appendChild(node_numbers)
    doc.appendChild(node_root)
    with open(filename, 'w') as f:
        doc.writexml(f, newl='\n', encoding='utf-8')

if __name__ == '__main__':
    data = read_xls('numbers.xls')
    j = json.dumps(data)
    formated = j.replace('[[', '[\n[').replace(']]', ']\n]').replace('], ', '],\n').replace('\n[', '\n    [')
    write_xml('numbers.xml', formated)
