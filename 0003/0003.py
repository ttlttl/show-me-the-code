# -*- coding: utf-8 -*-
"""第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""
import redis
import hashlib

s = 'B8#%lG^o@@.<_'

def gen_key(num=1, len=12):
    m = hashlib.md5()
    i = 0;
    while i < num:
        i = i + 1
        m.update((s+str(i)).encode('utf-8'))
        yield m.hexdigest()[0:len]


def save_to_redis_list(keys):
    r = redis.Redis('127.0.0.1')
    for k in keys:
        r.lpush('keys', k)
    results = r.lrange('keys', '0', '1000')
    for result in results:
        print(result)

if __name__ == '__main__':
    keys = gen_key(200, 12)
    save_to_redis_list(keys)