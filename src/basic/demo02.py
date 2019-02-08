# 静态路由和动态路由
# 先静态路由，后动态路由
from flask import Flask
app = Flask('__name__')
@app.route('/')
def index():
    return '<h1>root</h1>'
@app.route('/greet')
def greet():
    return '<h1>Hello everyone</h1>'
@app.route('/greet/lining1')
def greetLining():
    return '<h1>Hello lining</h1>'
# 动态路由
@app.route('/greet/<name>')
def greetName(name):
    return '<h1>hello my {}</h1>'.format(name)
@app.route('/greet/<a1>/<a2>/<a3>')
def args1(a1,a2,a3):
    return '<h1>{},{},{}</h1>'.format(a1,a2,a3)

@app.route('/greet/<a1>-<a2>-<a3>')
def args2(a1,a2,a3):
    return '<h1>{}*{}*{}</h1>'.format(a1,a2,a3)
if __name__ == '__main__':
    app.run()