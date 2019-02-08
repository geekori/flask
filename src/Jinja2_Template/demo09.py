# 使用Flask_Bootstrap模块集成Twitter Bootstrap
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('bs.txt',name='李宁')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')







