# 自定义错误页面

'''
404

500
'''

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/500')
def index():  
    raise Exception('服务器内部错误，请检查代码') 
    return render_template('error.txt',name='李宁')
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.txt'),404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.txt',error=e),500
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')

