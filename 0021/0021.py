# -*- coding: utf-8 -*-
"""
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
"""

import hashlib

SALT = '8#@ia0o'

def encrypt_password(password):
    sha1 = hashlib.sha1()
    password = password + SALT
    sha1.update(password.encode('utf-8'))
    return sha1.hexdigest()[3:33]

def validate_password(password, hashed):
    return encrypt_password(password) == hashed

def test():
    p = input('Password:')
    hashed = encrypt_password(p)
    print(hashed)
    print('Validation: %s' % validate_password(p, hashed))

if __name__ == '__main__':
    test()