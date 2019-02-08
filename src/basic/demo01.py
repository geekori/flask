'''
作者：李宁
官网：https://geekori.com

'''
# 用8行代码实现一个Web应用
from flask import Flask
from time import *
app = Flask(__name__)
@app.route('/')
def hello():
    return strftime('%Y-%m-%d %H:%M:%S',localtime(time()))
if __name__ == "__main__":
    app.run()
