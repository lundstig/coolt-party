from bottle import *
import data

site_path = "static/"

test_drink = dict(
    name="Testdrink",
    description="En lyxig drink...",
    ingredients=["1 cl vatten", "2 cl citronjuice"],
    reviews=["Mkt bra, 5/7", "Helt ok, 10/10"]
)

@get("/static/<filepath:path>")
def hello(filepath):
    return static_file(filepath, root=site_path)


@get("/")
def get_index():
    return static_file("index.html", root=site_path)


@get("/drink/<drink_id>")
def get_drink(drink_id):
    # drink = test_drink
    # drink = data.get_recipe("Testdrink")
    drink = data.get_recipes()[0]
    return template("recipe.tpl", drink)


data.connect()
# data.add_recipe(test_drink["name"], test_drink["description"], test_drink["ingredients"])
run(host="localhost", port=8080, reloader=True)
