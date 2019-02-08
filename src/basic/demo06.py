# 静态文件和重定向

from flask import *
app = Flask(__name__)

@app.route('/test')
def test():
    return app.send_static_file('test1.txt')

@app.route('/abc')
def abc():
    return redirect('/static/test1.txt')
if __name__ == '__main__':
    app.run()

