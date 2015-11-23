# -*- coding: utf-8 -*-
"""第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。？
"""
import mysql.connector
import hashlib

s = 'B8#%lG^o@@.<_'

def gen_key(num=1, len=12):
    m = hashlib.md5()
    i = 0;
    while i < num:
        i = i + 1
        m.update((s+str(i)).encode('utf-8'))
        yield m.hexdigest()[0:len]


conf = {
    'user' : 'test',
    'password' : 'test',
    'database' : 'test',
    'use_unicode' : True
}


create_table = """create table active_keys(
                      id int unsigned primary key auto_increment,
                      active_key varchar(32)
                  )"""


def save_to_mysql(keys):
    conn = mysql.connector.connect(**conf)
    print("Connected to database.")
    cursor = conn.cursor()
    cursor.execute('show tables')
    tables = cursor.fetchall()

    cursor.execute(create_table)

    try:
        for key in keys:
            cursor.execute('insert into active_keys (active_key) values("%s")' % key)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def query():
    conn = mysql.connector.connect(**conf)
    print("Connected to database.")
    cursor = conn.cursor()
    cursor.execute('select * from active_keys')
    keys = cursor.fetchall()
    conn.close()
    for key in keys:
        print(key)

if __name__ == '__main__':
    keys = gen_key(200, 12)
    save_to_mysql(keys)
    query()