import os
from flask import Flask, redirect, render_template
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

def get_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f"rgb({red}, {green}, {blue})"



@app.route('/')
def index():
  random_color = get_random_color()
  return render_template('/foods', random_color=random_color)

# @app.route('/')
# def index():
#   foods = sql('SELECT * FROM foods')
#   return render_template('foods/index.html', foods=foods) 






# mkdir app_app
# cd app_app
# python -m venv venv
# . venv/bin/activate
# flask --app planets run
# pip install Flask
# pip install requests

# flask --app app run --debug