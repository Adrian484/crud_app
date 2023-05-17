from db.db import sql

def all_foods():
  return sql('SELECT * FROM foods ORDER BY id')

def get_food(id):
  foods = sql("SELECT * FROM foods WHERE id = %s", [id])
  return foods[0]

def create_food(name, calories, protein, carbohydrates, image_url):
  sql('INSERT INTO foods(name, calories, protein, carbohydrates, image_url) VALUES(%s, %s, %s, %s, %s) RETURNING *', [name, calories, protein, carbohydrates, image_url])

def update_food(id, name, calories, protein, carbohydrates, image_url):
  sql('UPDATE foods SET name=%s, calories=%s, protein=%s, carbohydrates=%s, image_url=%s WHERE id=%s RETURNING *', [name, calories, protein, carbohydrates, image_url, id])

def delete_food(id):
  sql('DELETE FROM foods WHERE id=%s RETURNING *', [id])

def like_food(food_id, user_id):
  sql("INSERT INTO likes(user_id, food_id) VALUES(%s, %s) RETURNING *", [user_id, food_id])