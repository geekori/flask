# 条件控制
from flask import Flask,render_template
app = Flask(__name__)
'''
1.  如何写条件控制语句
2.  条件什么情况下为True，什么情况下为False

False、None、空列表、空字典、空字符串（Jinja2）
if condition:
    .......
elif condition:
    ......
else:
    ....

Jinja2模板条件为False的情况
1. 变量不存在
2. 字符串为空（长度为0）
3. 数值为0或0.0
4. 空列表
5. 空字典
6. None
'''


@app.route('/')
def index():
    return render_template('if.txt',user='Bill',
                           intValue = 0.0,
                           list = [1,2,3],
                           dict = {'a':'b'},
                           value = None)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')