# Radio、Select和SelectMultiple组件

from flask import Flask,request,render_template
from flask_wtf import FlaskForm
from wtforms import RadioField,SelectField,SelectMultipleField,SubmitField,validators
app = Flask(__name__)
app.secret_key ='sdjsldj4323sdsdfssfdf43434'

class ContactForm(FlaskForm):
    radio = RadioField('请选择一个',choices = [('值1','选项1'),('值2','选项2'),('值3','选项3')],
               validators = [validators.AnyOf(['值1','值2','值3'],'请选择一个值')])
    select = SelectField('请选择一个选项',choices=[('值1','选项1'),('值2','选项2'),('值3','选项3')],
                         validators = [validators.AnyOf(['值2'],'请选择第二项')])
    selectMultiple = SelectMultipleField('请选择多个选项',choices = [('值1','选项1'),('值2','选项2'),('值3','选项3')],
                                         validators=[validators.AnyOf([['值1','值2'],['值1','值3']],'只能选择前两项或第1项、第3项')])
    submit = SubmitField('提交')
@app.route('/', methods=['GET','POST'])
def contact():
    form = ContactForm()
    ok = False
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print('error')
        else:
            print('输入成功')
            ok = True
         
    return render_template('select.txt',form=form,ok=ok)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='1234')
