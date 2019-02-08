# 使用flash函数向客户端发送消息

from flask import Flask,request,render_template,flash
from flask_wtf import FlaskForm
from wtforms import TextField,IntegerField,TextAreaField,BooleanField,DateField,SubmitField,validators
app = Flask(__name__)
app.secret_key ='sdjsldj4323sdsdfssfdf43434'

class ContactForm(FlaskForm):
    name = TextField('姓名',[validators.Required('姓名必须输入')])
    age = IntegerField('年龄',[validators.Required('必须输入年龄'),
                             validators.NumberRange(10,30,'年龄必须在10到30之间')])
    birth = DateField('出生日期',[validators.Required('必须输入出生日期')])
    isStudent = BooleanField('是否为学生')
    resume = TextAreaField('简历',[validators.Length(10,200,'简历长度必须在10到200个字符之间')])
    submit = SubmitField('提交')
@app.route('/', methods=['GET','POST'])
def contact():
    form = ContactForm()
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print('error')
        else:
            flash('输入成功')
            flash('<h1>success</h1>')
            print('输入成功')
            ok = True
         
    return render_template('simple.txt',form=form,ok=ok)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')