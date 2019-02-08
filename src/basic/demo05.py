# 会话（Session）
from flask import Flask
from flask import request
from flask import session
from datetime import *

app = Flask(__name__)
@app.route('/')
def index():
    if 'username' in session:
        return '已经登录 %s' % session['username']
    return '未登录'
@app.route('/login')
def login():
    session.permanent = True
    session['username'] = request.args.get('username')
    return '登录成功'

@app.route('/logout')
def logout():
    session.pop('username',None)
    return '注销成功'
app.secret_key = 'dsfkhskhfkshfkshkfsk'
app.permanent_session_lifetime = timedelta(seconds = 20)

if __name__ == '__main__':
    app.run()

