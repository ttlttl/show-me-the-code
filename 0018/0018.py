# -*- coding: utf-8 -*-
"""
第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<cities>
<!--
    城市信息
-->
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
</cities>
</root>
"""
import xlrd
import json
from collections import OrderedDict
from xml.dom import minidom

def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    d = OrderedDict()
    for i in range(nrows):
        row = table.row_values(i)
        d[row[0]] = row[1:ncols]
    return d

def append_student_node(doc, father, elem):
    k, v = elem
    node_city = doc.createElement('city')
    node_city.setAttribute('id', k)
    node_city.appendChild(doc.createTextNode(v[0]))
    father.appendChild(node_city)

def write_xml(filename, data):
    doc = minidom.Document()
    node_root = doc.createElement('root')
    node_cities = doc.createElement('cities')
    node_comment = doc.createComment('城市信息\n')
    for elem in data.items():
        append_student_node(doc, node_cities, elem)
    node_root.appendChild(node_comment)
    node_root.appendChild(node_cities)
    doc.appendChild(node_root)
    with open(filename, 'w') as f:
        doc.writexml(f, newl='\n', encoding='utf-8')

if __name__ == '__main__':
    data = read_xls('city.xls')
    write_xml('city.xml', data)