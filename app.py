from flask import Flask
from flask import render_template 
from flask import request 
import psycopg2

app = Flask (__name__)

DB_URL = "dbname=food_nutrition_db"
def sql(query, parameters=[]):
  connection = psycopg2.connect(DB_URL) # open connection
  cursor = connection.cursor()
  cursor.execute(query, parameters) # begin transaction
  results = cursor.fetchall()
  connection.commit() # end transaction
  connection.close() # close connection
  return results



@app.route('/')
def index():
    foods = sql('SELECT * FROM foods')
    return render_template('index.html', foods=foods)

@app.route('/index', methods=["POST"])
def users_create():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')

    sql('INSERT INTO users(first_name, last_name, email) VALUES(%s, %s, %s,) RETURNING *', [first_name, last_name, email])
    return redirect('/')

@app.route('/signup')
def signup():
    return render_template('signup.html')





@app.route('/new')
def users_new():
    return render_template('/new.html')





# mkdir app_app
# cd app_app
# python -m venv venv
# . venv/bin/activate
# flask --app planets run
# pip install Flask
# pip install requests

# flask --app app run --debug