from bottle import *
import data

site_path = "static/"

test_drink = dict(
    name="Testdrink",
    description="En lyxig drink...",
    ingredients=["1 cl vatten", "2 cl citronjuice"],
    reviews=["Mkt bra, 5/7", "Helt ok, 10/10"]
)


def validate_form(form, required):
    errors = []
    for field in required:
        value = form.get(field)
        if value is "" or value is None:
            errors.append("Missing field {}".format(field))

    if errors:
        return ". ".join(errors)
     

@get("/static/<filepath:path>")
def hello(filepath):
    return static_file(filepath, root=site_path)


@get("/")
def get_index():
    return static_file("index.html", root=site_path)


    

@get("/recipes/<recipe_id>")
def get_recipe(recipe_id):
    recipe = data.get_recipe(recipe_id)
    if recipe is None:
        return abort(404, "Recipe not found")
    return template("recipe.tpl", recipe)



@get("/create/recipe")
def get_create_recipe():
    return template("create_recipe.tpl")


@post("/create/recipe")
def create_recipe():
    errors = validate_form(request.forms, ['name', 'description', 'ingredients'])
    if errors:
        return template("create_recipe.tpl", errors=errors)

    name = request.forms.name
    description = request.forms.description
    ingredients = request.forms.ingredients.splitlines()

    recipe_id = data.add_recipe(name, description, ingredients)
    redirect("/recipes/{}".format(recipe_id))
    


data.connect()
run(host="localhost", port=8080, reloader=True)
