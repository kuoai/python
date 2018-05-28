# -*- coding: utf-8 -*-
import pymysql
db=pymysql.connect("localhost","root","123456","hmh")
cursur=db.cursor()
cursur.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,SEX CHAR(1))"""
cursur.execute(sql)
db.close()