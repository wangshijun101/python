#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('sqlite://test.db',echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(id='5',name='Joseph')

session.add(new_user)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id == '5').one()
print 'type:',type(user)
print 'name:',user.name
session.close()

