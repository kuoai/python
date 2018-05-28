# 封装接口主要讲静态接口(无参数传入)、动态接口(有参数传入，不同参数返回的信息不同)
# 针对动态接口有三种传参方式：key_value,json串,拼接参数入参

# 封装成无参数传入的接口
from flask import Flask,jsonify,request
data = {
    "anna":{
        "age": 24,
        "sex": "女"
    },
    "lilei":{
        "age": 20,
        "age": "男"
    }
}

# 创建一个服务，赋值给app
app = Flask(__name__)

# 指定接口访问的路径，支持什么请求方式get,post
@app.route("/get_user", methods=["post"])    #请求的接口名称
# 讲的是封装成一种静态的接口，无任何参数传入

# 函数名字任意取
def get_user():
    return jsonify(data)       #把字典转成json串返回

app.run(host="10.10.11.121",port=8080,debug=True)

# 这个host：windows就是一个网卡，可以不写，而liux有多个网卡，写成0.0.0.0可以接受任意网卡信息
# 通过访问本地127.0.0.1:8080/get_user可返回data信息
# debug调试的时候可以指定debug=true,如果提供接口给他人使用的时候，debug要去掉


