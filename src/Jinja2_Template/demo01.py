# Jinja2模板入门

# Web模板 =  HTML页面（js、css、html代码）+动态部分

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    return render_template('user.txt', name1=name)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')