import os
from flask import Flask, redirect, request, render_template
from routes.foods_routes import foods_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
from dotenv import load_dotenv
from controllers.foods_controller import index as foods_index
from models.food import calorie_amount, all_foods
from services.session_info import current_user

load_dotenv()

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(foods_routes, url_prefix='/foods')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def redirect_to_foods():
    return redirect('/foods')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        max_calories = request.form.get('calorie_amount')
        if max_calories:
            foods = calorie_amount(max_calories)
        else:
            foods = all_foods()
        return render_template('foods/index.html', foods=foods, current_user=current_user())
    else:
        # Handle GET request, retrieve all foods
        foods = all_foods()
        return render_template('foods/index.html', foods=foods, current_user=current_user())




# mkdir app_app
# cd app_app
# python -m venv venv
# . venv/bin/activate
# flask --app app run
# pip install Flask
# pip install requests

# flask --app app run --debug