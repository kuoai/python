# -*- coding: utf-8 -*-
import MySQLdb
db = MySQLdb.connect("localhost", "root", "123456", "hmh")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print("Database version : %s " % data)
db.close()

