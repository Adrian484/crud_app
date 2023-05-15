from flask import render_template, request, redirect
from models.food import all_foods, get_food, create_food, update_food, delete_food

def index():
  foods = all_foods()
  return render_template('foods/index.html', foods=foods)

def new():
  return render_template('foods/new.html')

def create():
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  create_food(name, image_url)
  return redirect('/')

def edit(id):
  food = get_food(id)
  return render_template('foods/edit.html', food=food)

def update(id):
  name = request.form.get('name')
  image_url = request.form.get('image_url')
  update_food(id, name, image_url)
  return redirect('/')

def delete(id):
  delete_food(id)
  return redirect('/')