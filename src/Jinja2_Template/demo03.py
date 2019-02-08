# Jinja2模板的过滤器

'''
Jinja2支持的过滤器

safe：渲染值时不转义
capitalize：把值的首字母转换成大写，其他字母都转换成小写
lower：把值的所有字母都变成小写
upper：把值的所有字母都变成大写
title：把值中每个单词的首字母都转换成大写
trim：把值的首尾空格去掉
striptags：渲染之前将值中所有的HTML标签都去掉

'''

from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('filter.txt',name='bill',value='I love python.')
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')