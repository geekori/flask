# 在Jinja2模板中使用复杂的数据

from flask import Flask,render_template

app = Flask(__name__)

class MyClass:
    def func(self):
        return 'func'
def myfunc():
    return 'myfunc'
@app.route('/')
def index():
    mydict = {}
    mydict['type'] = 'dict'
    mylist = []
    mylist.append('list')
    myclass = MyClass()
    return render_template('template.txt', mydict = mydict,
                           mylist = mylist, myclass=myclass,
                           myfunc = myfunc)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')