from flask import Flask
from flask import render_template 
from flask import request 


app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# mkdir app_app
# cd app_app
# python -m venv venv
# . venv/bin/activate
# flask --app planets run
# pip install Flask
# pip install requests

# flask --app app run --debug