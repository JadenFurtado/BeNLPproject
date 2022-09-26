from joblib import PrintTime
from app import app
from flask import render_template,request
import mysql.connector

@app.route("/signup")
def displaySignupPage():
    return render_template("signup/user.html")
        
@app.route("/signup/user",methods=["POST"])
def signupUser():
    userName = request.form.get("userName")
    userPassword = request.form.get("userPassword")
    userEmail = request.form.get("userEmail")
    userPhoneNumber = request.form.get("userPhoneNumber")
    try:
        mydb = mysql.connector.connect(host=app.config['DB_HOST'],user=app.config['DB_USERNAME'],password=app.config['DB_PASSWORD'],database=app.config['DB_NAME'])
        print(app.config['DB_HOST'])
        mycursor = mydb.cursor()
        print(mycursor)
        print("success")
        sql = "INSERT INTO usersData (userName, userPassword, userEmail, userPhoneNumber) VALUES (%s, %s, %s, %s)"
        val = (userName,userPassword,userEmail,userPhoneNumber)
        mycursor.execute(sql, val)
        print(mycursor)
        mydb.commit()
    except:
        print(mycursor)
        print("error")
        mydb.rollback()
    return "success"

