# -*- coding: utf-8 -*-
"""第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。？
"""
import hashlib
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

s = 'B8#%lG^o@@.<_'

def gen_key(num=1, len=12):
    m = hashlib.md5()
    i = 0;
    while i < num:
        i = i + 1
        m.update((s+str(i)).encode('utf-8'))
        yield m.hexdigest()[0:len]

class Key(Base):
    __tablename__ = 'act_keys'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    key = Column(String(32))
    def __repr__(self):
        return "Key(id = %d, key = %s" % (self.id, self.key)

engine = create_engine('mysql+mysqlconnector://test:test@localhost/test', echo=True)
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

if __name__ == '__main__':
    keys = gen_key(200, 12)
    session = DBSession()
    for k in keys:
        new_key = Key(key=k)
        session.add(new_key)
    session.commit()
    session.close()

    session = DBSession()
    keys = session.query(Key)
    for k in keys:
        print(k)