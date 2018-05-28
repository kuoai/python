import pymysql
# 查询操作

# 打开数据库
db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="hmh")

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql查询语句， user对应表名
sql = "select * from user"
try:
    cur.execute(sql)        #执行sql语句
    results = cur.fetchall()        #获取查询的所有记录
    print("id","username","area")

    # 遍历结果
    for row in results:
        id = row[0]
        name = row[1]
        area = row[2]
        print(id,name,area)
except Exception as e:
    raise e
finally:
    db.close()      #关闭数据库
