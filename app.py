import os
from flask import Flask, redirect, request, render_template
from routes.foods_routes import foods_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
import random

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(foods_routes, url_prefix='/foods')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')




@app.route('/')
def index():
  return redirect('/foods')




# mkdir app_app
# cd app_app
# python -m venv venv
# . venv/bin/activate
# flask --app planets run
# pip install Flask
# pip install requests

# flask --app app run --debug