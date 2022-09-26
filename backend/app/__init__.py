from os import environ
from flask import Flask
from os import environ

app = Flask(__name__)
app.config['DB_USERNAME'] = environ.get("DB_USERNAME")
app.config['DB_PASSWORD'] = environ.get("DB_PASSWORD")
app.config['DB_NAME'] = environ.get("DB_NAME")
app.config['DB_HOST'] = environ.get("DB_HOST")

# from app import signup_view
# from app import login_view
# from app import save_view
from app import home_view
