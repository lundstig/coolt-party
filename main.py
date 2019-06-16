from bottle import *
import os

import data

# pylint: disable=no-member

SITE_PATH = "static/"


def validate_form(form, required):
    errors = []
    for field in required:
        value = form.get(field)
        if not value:
            errors.append("Missing field {}".format(field))

    if errors:
        return ". ".join(errors)
    return None


@get("/static/<filepath:path>")
def hello(filepath):
    return static_file(filepath, root=SITE_PATH)


@get("/")
def get_index():
    return static_file("index.html", root=SITE_PATH)

@get("/recipes")
def get_recipes():
    recipes = data.get_recipes()
    return template("recipes.tpl", {"recipes": recipes})

@get("/recipes/<recipe_id:int>")
def get_recipe(recipe_id):
    recipe = data.get_recipe(recipe_id)
    if recipe is None:
        return abort(404, "Recipe not found")
    return template("recipe.tpl", recipe)


@post("/recipes/<recipe_id:int>")
def review_recipe(recipe_id):
    errors = validate_form(request.forms, ["review", "author", "rating"])
    valid_ratings = ["1/5", "2/5", "3/5", "4/5", "5/5"]
    rating = request.forms.rating
    print(rating)
    if not errors and data.get_recipe(recipe_id) and rating in valid_ratings:
        numeric_rating = int(rating[0])
        data.add_review(recipe_id, request.forms.review, request.forms.author, numeric_rating)
    redirect("/recipes/{}".format(recipe_id))


@get("/create/recipe")
def get_create_recipe():
    return template("create_recipe.tpl")


@post("/create/recipe")
def create_recipe():
    errors = validate_form(request.forms, ["name", "description", "ingredients"])
    if errors:
        return template("create_recipe.tpl", errors=errors)

    name = request.forms.name
    description = request.forms.description
    ingredients = request.forms.ingredients.splitlines()

    recipe_id = data.add_recipe(name, description, ingredients)
    return redirect("/recipes/{}".format(recipe_id))

DEBUG_MODE = os.environ.get('PROD') is None
PASSWORD = os.environ.get('PASSWORD')
print(f"DEBUG_MODE = {DEBUG_MODE}")
if not PASSWORD:
    print("No password provided in envvar PASSWORD!")
    exit(1)

debug(DEBUG_MODE)
data.connect(password=PASSWORD)
run(host="0.0.0.0", port=8080, reloader=DEBUG_MODE)
