# -*- coding: utf-8 -*-
import pymysql
db=pymysql.connect("localhost","root","123456","hmh")
cursur=db.cursor()
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX) VALUES ("HMH","MHMH",23,"M")"""
try:
    cursur.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()