import pymysql
# 更新操作

# 打开数据库
db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="hmh")


# 使用cursou()方法获取操作游标
cur = db.cursor()

sql_update = """update use set username = '%s' where id = '%d'"""
try:
    cur.execute(sql_update % ("lz",))
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()

