from db.db import sql

def all_foods():
  return sql('SELECT * FROM foods ORDER BY id')

def get_food(id):
  foods = sql("SELECT * FROM foods WHERE id = %s", [id])
  return foods[0]

def create_food(name, image_url):
  sql('INSERT INTO foods(name, image_url) VALUES(%s, %s) RETURNING *', [name, image_url])

def update_food(id, name, image_url):
  sql('UPDATE foods SET name=%s, image_url=%s WHERE id=%s RETURNING *', [name, image_url, id])

def delete_food(id):
  sql('DELETE FROM foods WHERE id=%s RETURNING *', [id])

def like_food(food_id, user_id):
  sql("INSERT INTO likes(user_id, food_id) VALUES(%s, %s) RETURNING *", [user_id, food_id])