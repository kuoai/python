# 给url添加变量部分，你可以把这些特殊的字段标记为<variable_name>，这个部分将会作为命名参数传递到你的函数
# 规则可以用<converter:variable_name>指定一个可选的的转换器
# int 接受整数
# float 用int,但是接受浮点数
# path  和默认的相似，但也接受斜线

from flask import Flask
app=Flask(__name__)
@app.route("/user/<username>")
def show_user_profile(username):
    return "user %s" % username

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post %d" % post_id

if __name__=="__main__":
    # app.debug = True
    app.run(debug=True)