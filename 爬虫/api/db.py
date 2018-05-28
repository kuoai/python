import pymysql
from flask import Flask,jsonify,request

conn=pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='hmh')
cur=conn.cursor()#获取一个游标
sql_select = "select * from employee"#定义查询
cur.execute(sql_select) #执行查询
print(sql_select)
data =cur.fetchall() #获取查询到数据
#cur.fetchone()获取一条数据
for i in range(len(data)):
    print(data[i])

app = Flask(__name__)
@app.route("/get_user",methods=["POST"])

# 请求后直接拼接入参方式
def get_user():
    return jsonify(data)

app.run(host="127.0.0.1",port=8080,debug=True)


conn.commit()#提交事务
cur.close()#关闭游标
conn.close()#释放数据库资源