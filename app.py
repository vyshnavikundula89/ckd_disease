from flask import Flask,request, url_for, redirect, render_template
import pandas as pd
import numpy as np
import pickle
import sqlite3

app = Flask(__name__)

model_name = open("model.pkl","rb")
model = pickle.load(model_name)



@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')

@app.route("/signup")
def signup():

    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("index.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index.html")
    else:
        return render_template("signup.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    text1 = request.form['1']
    text2 = request.form['2']
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']
    text9 = request.form['9']
    text10 = request.form['10']
    text11 = request.form['11']
    text12 = request.form['12']
    text13 = request.form['13']
    text14 = request.form['14']
    text15 = request.form['15']
    text16 = request.form['16']
    text17 = request.form['17']
    text18 = request.form['18']
    text19 = request.form['19']
    text20 = request.form['20']
    text21 = request.form['21']
    text22 = request.form['22']
    text23 = request.form['23']
    text24 = request.form['24']
    row_df = np.array([text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20,text21,text22,text23,text24])
    row_df  = row_df.reshape(1,-1)
    prediction=model.predict(row_df)
    if prediction == 1:
        return render_template('result.html',pred=f'You have chance of having Chronic Kidney Disease')
    else:
        return render_template('result.html',pred=f'You are safe! You do not have Disease')



@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/note')
def note():
	return render_template('notebook.html')


if __name__ == '__main__':
    app.run(debug=True)
