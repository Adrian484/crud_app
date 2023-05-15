from flask import Flask, redirect
from routes.foods_routes import foods_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

app = Flask(__name__)

app.register_blueprint(foods_routes, url_prefix='/foods')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')


@app.route('/')
def index():
    return redirect('/foods')

@app.route('/foods/new')
@app.route('/foods', methods=['POST'])
@app.route('/foods/<id>/edit')
@app.route('/foods/<id>', methods=["POST"])
@app.route('/foods/<id>/delete', methods=["POST"])

@app.route('/users/new')
@app.route('/users', methods=["POST"])





# mkdir app_app
# cd app_app
# python -m venv venv
# . venv/bin/activate
# flask --app planets run
# pip install Flask
# pip install requests

# flask --app app run --debug