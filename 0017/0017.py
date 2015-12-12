# -*- coding: utf-8 -*-
"""
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
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
    node_student = doc.createElement('student')
    node_student.setAttribute('id', k)
    node_name = doc.createElement('name')
    node_name.appendChild(doc.createTextNode(v[0]))
    node_scores = doc.createElement('scores')
    node_c = doc.createElement('chinese')
    node_c.appendChild(doc.createTextNode(str(v[1])))
    node_m = doc.createElement('math')
    node_m.appendChild(doc.createTextNode(str(v[2])))
    node_e = doc.createElement('english')
    node_e.appendChild(doc.createTextNode(str(v[3])))
    node_student.appendChild(node_name)
    node_scores.appendChild(node_c)
    node_scores.appendChild(node_m)
    node_scores.appendChild(node_e)
    node_student.appendChild(node_scores)
    father.appendChild(node_student)

def write_xml(filename, data):
    doc = minidom.Document()
    node_root = doc.createElement('root')
    node_students = doc.createElement('students')
    node_comment = doc.createComment('学生信息表\n"id" : [名字，数学，语文，英文]\n')
    for elem in data.items():
        append_student_node(doc, node_students, elem)
    node_root.appendChild(node_comment)
    node_root.appendChild(node_students)
    doc.appendChild(node_root)
    with open(filename, 'w') as f:
        doc.writexml(f, newl='\n', encoding='utf-8')

if __name__ == '__main__':
    data = read_xls('students.xls')
    write_xml('students.xml', data)