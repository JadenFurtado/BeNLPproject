from joblib import PrintTime
from app import app
from flask import render_template,request
import mysql.connector

@app.route("/login")
def displayLoginPage():
    return render_template("login/user.html")
        
@app.route("/login/user",methods=["GET"])
def loginUser():
    data = ""
    try:
        mydb = mysql.connector.connect(host=app.config['DB_HOST'],user=app.config['DB_USERNAME'],password=app.config['DB_PASSWORD'],database=app.config['DB_NAME'])
        print(app.config['DB_HOST'])
        mycursor = mydb.cursor()
        print(mycursor)
        print("success")
        sql = "SELECT userName, userPassword, userEmail, userPhoneNumber FROM usersData WHERE id=%s"
        val = (1)
        data = mycursor.fetchone(sql, val)
        print(mycursor)
        print(data)
    except:
        print(mycursor)
        print("error")
    mydb = mysql.connector.connect(host=app.config['DB_HOST'],user=app.config['DB_USERNAME'],password=app.config['DB_PASSWORD'],database=app.config['DB_NAME'])
    print(app.config['DB_HOST'])
    mycursor = mydb.cursor()
    print(mycursor)
    print("success")
    sql = "SELECT userName, userPassword, userEmail, userPhoneNumber FROM usersData WHERE id=%s"
    val = ("1")
    mycursor.execute(sql, val)
    data = mycursor.fetchone()
    print(mycursor)
    print(data)
    return data

