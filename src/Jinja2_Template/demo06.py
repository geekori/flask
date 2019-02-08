# 宏操作
from flask import Flask,render_template
app = Flask(__name__)


class MyItem:
    def __init__(self,id,name):
        self.id = id
        self.name = name
@app.route('/')
def index():
    return render_template('macro.txt',
                           items1=[MyItem(100,'Hello'),
                                  {'id':2,'name':'John'},
                                   {'id':3,'name':'Mary'}],
                            items2=[MyItem(200,'World'),
                                  MyItem(400,'New')
                                   ],
                           items3=(MyItem(800,'123'),
                                  MyItem(1600,'Horse')
                                   ))
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')