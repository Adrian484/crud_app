from flask import render_template, request, redirect, session
from models.food import all_foods, get_food, create_food, update_food, delete_food, like_food, calorie_amount
from services.session_info import current_user
import random

def index():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    print(request.method)  # Debug print statement
    print(request.form) 

    max_calories = request.form.get('calorie_amount')  # Get the maximum calorie amount from the form submission

    if max_calories:  # If a maximum calorie amount is provided, call the calorie_amount function
        foods = calorie_amount(max_calories)
    else:  # Otherwise, retrieve all foods
        foods = all_foods()

    return render_template('foods/index.html', random_color=random_color, foods=foods, current_user=current_user())

def new():
  return render_template('foods/new.html')

def create():
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  calories = request.form.get('calories')
  protein = request.form.get('protein')
  carbohydrates = request.form.get('carbohydrates')

  create_food(name, calories, protein, carbohydrates, image_url)
  return redirect('/')

def edit(id):
  food = get_food(id)
  return render_template('foods/edit.html', food=food)

def update(id):
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  calories = request.form.get('calories')
  protein = request.form.get('protein')
  carbohydrates = request.form.get('carbohydrates')

  update_food(id, name, calories, protein, carbohydrates, image_url)
  return redirect('/')

def delete(id):
  delete_food(id)
  return redirect('/')

def like(id):
  like_food(id, session['user_id'])
  return redirect('/')