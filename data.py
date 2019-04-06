import dataset

db_url = 'lundstig.com:5432'
db_user = 'db'
db_password = '5YCDON1nPLDUXynSoLYOv5TttYsNDGiN'
db_name = 'db'

db = None
recipes = None
ingredients = None

def connect():
    global db
    global recipes
    global ingredients
    url = 'postgresql://{}:{}@{}/{}'.format(db_user, db_password, db_url, db_name)
    db = dataset.connect(url)
    recipes = db['recipes']
    ingredients = db['ingredients']

def get_recipes():
    ret = []
    for recipe in recipes:
        recipe.ingredients = map(lambda row: row.ingredient, ingredients.find(name=recipe.name))
    return ret


def add_recipe(name, description, ingredients, reviews=[]):
    recipes.insert(dict(name=name, desription=description))
    for ingredient in ingredients:
        ingredients.insert(dict(name=name, ingredient=ingredient))

