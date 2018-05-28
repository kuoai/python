# 有参数传入的接口
# 3.请求链接直接拼接入参方式
from flask import Flask,jsonify,request
data = {
    "nana":{
        "age": 24,
        "sex": "女"
    },
    "lilei":{
        "age": 21,
        "sex": "男"
    }
}
msg = {
    "msg": "不存在的用户名"
}

app = Flask(__name__)
@app.route("/get_user",methods=["POST"])

# 请求后直接拼接入参方式
def get_user():
    # 使用request.args.get方式获取拼接的入参数据
    username = request.args.get('username')
    # 判断请求传入的参数是否在字典里
    if username in data:
        return jsonify(data[username])      #如果在的话，则返回data对应key的值转成json串信息
    else:
        return jsonify(msg)      #如果不在的话，返回err对应key的value转成json串信息

app.run(host="127.0.0.1",port=8080,debug=True)