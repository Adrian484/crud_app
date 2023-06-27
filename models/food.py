from db.db import sql
from flask import request
import psycopg2

def all_foods():
  return sql('SELECT * FROM foods ORDER BY id')

def get_food(id):
  foods = sql("SELECT * FROM foods WHERE id = %s", [id])
  return foods[0]

def calorie_amount(calories):
  foods = sql("SELECT * FROM foods WHERE calories <= %s;", [calories])
  return foods

# def calorie_amount(max_calories):
#     conn = psycopg2.connect(database="food_nutrition_db")
#     cur = conn.cursor()
#     query = "SELECT * FROM foods WHERE calories <= %s;"
#     cur.execute(query, (max_calories,))
#     foods = cur.fetchall()
#     cur.close()
#     conn.close()
#     # Convert the result to a list of dictionaries
#     food_list = []
#     for food in foods:
#         food_dict = {
#             'id': food[0],
#             'name': food[1],
#             'calories': food[2],
#             'protein': food[3],
#             'carbohydrates': food[4],
#             'image_url': food[5]
#         }
#         food_list.append(food_dict)
#     return food_list
  
def create_food(name, calories, protein, carbohydrates, image_url):
  sql('INSERT INTO foods(name, calories, protein, carbohydrates, image_url) VALUES(%s, %s, %s, %s, %s) RETURNING *', [name, calories, protein, carbohydrates, image_url])

def update_food(id, name, calories, protein, carbohydrates, image_url):
  sql('UPDATE foods SET name=%s, calories=%s, protein=%s, carbohydrates=%s, image_url=%s WHERE id=%s RETURNING *', [name, calories, protein, carbohydrates, image_url, id])

def delete_food(id):
  sql('DELETE FROM foods WHERE id=%s RETURNING *', [id])

def like_food(food_id, user_id):
  sql("INSERT INTO likes(user_id, food_id) VALUES(%s, %s) RETURNING *", [user_id, food_id])