from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template('home.html', title_name='welcome')

@app.route('/service')
def service():
    return 'service'

@app.route('/about')
def about():
    return 'about'


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True)