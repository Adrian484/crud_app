from db.db import sql
from flask import request
import psycopg2

def all_foods():
  return sql('SELECT * FROM foods ORDER BY id')

def get_food(id):
  foods = sql("SELECT * FROM foods WHERE id = %s", [id])
  return foods[0]

def calorie_amount():
    # Get the calorie amount from the form submission
    calorie_amount = int(request.form['calorie_amount'])

    # Make a connection to the database
    conn = psycopg2.connect(database="food_nutrition_db")

    # Create a cursor object
    cur = conn.cursor()

    # Prepare the SQL query with a parameter
    query = "SELECT * FROM foods WHERE calories <= %s;"

    # Execute the query with the parameter
    cur.execute(query, (calorie_amount,))

    # Fetch the results
    foods = cur.fetchall()

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Return the foods
    return foods
  






def create_food(name, calories, protein, carbohydrates, image_url):
  sql('INSERT INTO foods(name, calories, protein, carbohydrates, image_url) VALUES(%s, %s, %s, %s, %s) RETURNING *', [name, calories, protein, carbohydrates, image_url])


def update_food(id, name, calories, protein, carbohydrates, image_url):
  sql('UPDATE foods SET name=%s, calories=%s, protein=%s, carbohydrates=%s, image_url=%s WHERE id=%s RETURNING *', [name, calories, protein, carbohydrates, image_url, id])

def delete_food(id):
  sql('DELETE FROM foods WHERE id=%s RETURNING *', [id])

def like_food(food_id, user_id):
  sql("INSERT INTO likes(user_id, food_id) VALUES(%s, %s) RETURNING *", [user_id, food_id])