import pymysql
# 插入操作

# 打开数据库
db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="hmh")


# 使用cursou()方法获取操作游标
cur = db.cursor()

sql_insert = """inster into user(id,username,area) values(3,'xhj','tianjin')"""
try:
    cur.execute(sql_insert)
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()

