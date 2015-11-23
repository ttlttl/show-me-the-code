# -*- coding: utf-8 -*-
"""第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
   使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import hashlib

s = 'B8#%lG^o@@.<_'

def gen_key(num=1, len=12):
    m = hashlib.md5()
    i = 0;
    while i < num:
        i = i + 1
        m.update((s+str(i)).encode('utf-8'))
        yield m.hexdigest()[0:len]

if __name__ == '__main__':
    keys = gen_key(200, 7)
    for key in keys:
        print(key)
