# -*- coding: utf-8 -*-
"""
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」
然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
"""
import xlrd
from collections import namedtuple


def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    Record = namedtuple('Record', table.row_values(0))
    return [Record(*table.row_values(i)) for i in range(1, table.nrows)]


def str2seconds(s):
    return eval(s.replace('时', '*60*60+').replace('分', '*60+').replace('秒', ''))


def seconds2str(d):
    return ('%s分%s秒' % (d // 60, d % 60))


def statistics(records):
    send = {}
    receive = {}
    for r in records:
        if r.呼叫类型 == '主叫':
            if r.对方号码 not in send.keys():
                send[r.对方号码] = str2seconds(r.通话时长)
            else:
                send[r.对方号码] += str2seconds(r.通话时长)
        if r.呼叫类型 == '被叫':
            if r.对方号码 not in receive.keys():
                receive[r.对方号码] = str2seconds(r.通话时长)
            else:
                receive[r.对方号码] += str2seconds(r.通话时长)
    send = [(k,v) for k, v in send.items()]
    receive = [(k,v) for k, v in receive.items()]
    def _f(t):
        return t[1]
    return sorted(send, key=_f, reverse=True), sorted(receive, key=_f, reverse=True)


if __name__ == '__main__':
    data = read_xls('records.xls')
    send, receive = statistics(data)
    print(send)
    print('主叫：')
    for (k,v) in send:
        print('号码 %s 通话时长: %s' % (k, seconds2str(v)))
    print('\n\n')
    print('被叫：')
    for k, v in receive:
        print('号码 %s 通话时长: %s' % (k, seconds2str(v)))
