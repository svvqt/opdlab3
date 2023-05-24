from flask import Flask, render_template, request
import file

app=Flask(__name__)
@app.route('/')
@app.route('/index')

def index():
    return render_template("log_in_page.html")

@app.route('/login',methods=['GET','POST'])
def login():
    n = 0
    users, passwords = file.importingfile()
    global userlogin,userpassword
    if request.method=='POST':
        userlogin=str(request.form.get('login'))
        userpassword=str(request.form.get('password'))
    if userlogin != 'None' and userpassword != 'None':
        if userlogin not in users:
            return render_template('log_in_page.html', error='Пользователь не обнаружен')
        else:
            for i in users:
                if userlogin==i:
                    needlogin=i
                    break
                else:
                    n+=1
            needpass=passwords[n]
            if userlogin==needlogin and userpassword==needpass:
                return render_template('user.html', login=userlogin, password=userpassword)
    return render_template('log_in_page.html', error='Неправильный пароль')

@app.route('/regi',methods=['GET','POST'])
def gotoreg():
    return render_template("reg.html")
@app.route('/registration',methods=['GET','POST'])
def reg():
    global userlogin,userpassword
    if request.method=='POST':
        userlogin=str(request.form.get('login'))
        userpassword=str(request.form.get('password'))
    users, passwords = file.importingfile()
    if userlogin not in users:
        f=open('users.txt','a')
        f.write(userlogin+" ")
        f.write(userpassword+'\n')
        f.close()
        return render_template('user.html',login=userlogin,password=userpassword)
    else:
        return render_template('reg.html',error='Имя пользователя занято')

@app.route('/back',methods=['GET','POST'])
def back():
    return render_template('log_in_page.html')

@app.route('/log_out')
def log_out():
    userlogin = ''
    userpassword = ''
    return render_template('log_in_page.html')
if __name__ == '__main__':
    app.run()
