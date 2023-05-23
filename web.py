from flask import Flask, render_template, request
import file

app=Flask(__name__)
@app.route('/')
@app.route('/index')

def index():
    return render_template("log_in_page.html")

@app.route('/login',methods=['GET','POST'])
def login():
    users, passwords = file.importingfile()
    global userlogin,userpassword
    if request.method=='POST':
        userlogin=str(request.form.get('login'))
        userpassword=str(request.form.get('password'))
    if userlogin != 'None' and userpassword != 'None':
        if userlogin not in users:
            return render_template('log_in_page.html', error='Пользователь не обнаружен')
        else:
            if userpassword not in passwords:
                return render_template('log_in_page.html',error='Неправильный пароль')
    return render_template('user.html',login=userlogin,password=userpassword)
@app.route('/regi',methods=['GET','POST'])
def gotoreg():
    return render_template("reg.html")
@app.route('/registration',methods=['GET','POST'])
def reg():
    global userlogin,userpassword
    if request.method=='POST':
        userlogin=str(request.form.get('login'))
        userpassword=str(request.form.get('password'))
    f=open('users.txt','a')
    f.write(userlogin+" ")
    f.write(userpassword+'\n')
    f.close()
    return render_template('user.html',login=userlogin,password=userpassword)



@app.route('/log_out')
def log_out():
    userlogin = ''
    userpassword = ''
    return render_template('log_in_page.html')
if __name__ == '__main__':
    app.run()