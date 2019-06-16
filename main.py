from bottle import *

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


@get("/recipes/<recipe_id:int>")
def get_recipe(recipe_id):
    recipe = data.get_recipe(recipe_id)
    if recipe is None:
        return abort(404, "Recipe not found")
    return template("recipe.tpl", recipe)


@post("/recipes/<recipe_id:int>")
def review_recipe(recipe_id):
    errors = validate_form(request.forms, ["review", "author"])
    if not errors and data.get_recipe(recipe_id):
        data.add_review(recipe_id, request.forms.review, request.forms.author)
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


debug(True)
data.connect()
run(host="localhost", port=8080, reloader=True)
