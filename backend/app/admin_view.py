from joblib import PrintTime
from app import app
from flask import render_template,request

@app.route("/login")
def displayLoginPage():
    return render_template("login/user.html")
