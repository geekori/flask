# 获取客户端请求（Request)
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s</h1>' % user_agent
@app.route('/abc')
def abc():
    value = request.args.get('arg')
    return '<h1>arg = %s</h1>' % value
if __name__ == '__main__':
    app.run()