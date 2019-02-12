from flask_mail import Mail, Message
from flask import Flask, flash, redirect, url_for, render_template, request,make_response
import os
app = Flask(__name__)


'''
SMTP

pip install flask-mail
'''

app.config.update(
    MAIL_SERVER='smtp.126.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=os.getenv('USERNAME'),
    MAIL_PASSWORD=os.getenv('PASSWORD')
)


mail = Mail(app)

@app.route('/sendmail',methods=['POST'])
def sendmail():
    email = request.form.get('email')
    subject = request.form.get('subject')
    body = request.form.get('body')

    message = Message(subject,recipients=[email],sender=('李宁','lntoto@126.com'),body=body)
    mail.send(message)

    response = make_response('已经成功发送email.')
    return response
@app.route('/sendHTML',methods=['POST'])
def sendhtml():
    email = request.form.get('email')
    subject = request.form.get('subject')
    body = request.form.get('body')

    message = Message(subject,recipients=[email],sender=('李宁','lntoto@126.com'),html=body)
    mail.send(message)

    response = make_response('已经成功发送email.')
    return response
@app.route('/',methods=['GET'])
def index():
    return render_template('sender.html')
if __name__ == "__main__":
    app.run(host='127.0.0.1',port='1234')

