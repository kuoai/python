# 有参数传入的接口
# 2.通过json串方式传参
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

# json方式传参
def get_user():
    # 获取带json串请求的username参数传入的值
    username1 = request.json.get('username1')
    # 判断请求传入的参数是否在字典里
    if username1 in data:
        return jsonify(data[username1])      #如果在的话，则返回data对应key的值转成json串信息
    else:
        return jsonify(msg)      #如果不在的话，返回err对应key的value转成json串信息

app.run(host="127.0.0.1",port=8080,debug=True)
