import dataset
import traceback

db_url = 'albert.lundstig.com:5432'
db_user = 'cooltparty'
db_password = '5YCDON0nPLDUXynSoLYOv5TttYsNDGiN'
db_name = 'cooltparty'

db = None
db_recipes = None
db_ingredients = None

def connect():
    global db
    global db_recipes
    global db_ingredients
    global db_reviews
    url = 'postgresql://{}:{}@{}/{}'.format(db_user, db_password, db_url, db_name)
    db = dataset.connect(url)
    db_recipes = db['recipes']
    db_ingredients = db['ingredients']
    db_reviews = db['reviews']

def populate_recipe(recipe):
    ingredients = db_ingredients.find(recipe=recipe['id'])
    recipe['ingredients'] = [row['ingredient'] for row in ingredients]
    reviews = db_reviews.find(recipe=recipe['id'])
    recipe['reviews'] = [row['review'] for row in reviews]

def get_recipes():
    ret = []
    for recipe in db_recipes:
        populate_recipe(recipe)
    return ret

def get_recipe(recipe_id):
    ret = db_recipes.find_one(id=recipe_id) 
    if ret is None:
        return None
    populate_recipe(ret)
    return ret


def add_recipe(name, description, ingredients, reviews=[]):
    db.begin()
    try:
        recipe_id = db_recipes.insert(dict(name=name, description=description))
        for ingredient in ingredients:
            db_ingredients.insert(dict(recipe=recipe_id, ingredient=ingredient))
        for review in reviews:
            db_reviews.insert(dict(recipe=recipe_id, review=review))
        db.commit()
        return recipe_id
    except Exception as e:
        db.rollback()
        traceback.print_exc()

