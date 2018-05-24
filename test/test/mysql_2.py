# -*- coding: utf-8 -*-
import pymysql
db = pymysql.connect("localhost", "root", "123456", "abc")
cursor = db.cursor()
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('hmh', 'hmh', 20, 'M', 2000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 关闭数据库
db.close()

