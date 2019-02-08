# 循环控制
from flask import Flask,render_template
app = Flask(__name__)

class MyItem:
    def __init__(self,id,name):
        self.id = id
        self.name = name
@app.route('/')
def index():
    return render_template('for.txt',products = ['iPhone9 Plus','特斯拉','兰博基尼','Bike'],
                           items=[MyItem(100,'Hello'),
                                  {'id':2,'name':'John'},
                                   {'id':3,'name':'Mary'}])
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')