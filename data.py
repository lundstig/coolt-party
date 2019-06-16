import dataset
import traceback

DB_URL = "albert.lundstig.com:5432"
DB_USER = "cooltparty"
DB_NAME = "cooltparty"

db = None
db_recipes = None
db_ingredients = None
db_reviews = None


def connect(password):
    global db
    global db_recipes
    global db_ingredients
    global db_reviews
    url = "postgresql://{}:{}@{}/{}".format(DB_USER, password, DB_URL, DB_NAME)
    print("Connecting to database...")
    db = dataset.connect(url)
    print("Connected! (not fully)")
    db_recipes = db["recipes"]
    db_ingredients = db["ingredients"]
    db_reviews = db["reviews"]


def populate_recipe(recipe):
    ingredients = db_ingredients.find(recipe=recipe["id"])
    recipe["ingredients"] = [row["ingredient"] for row in ingredients]
    recipe["reviews"] = db_reviews.find(recipe=recipe["id"])
    recipe["link"] = "/recipes/{}".format(recipe["id"])


def get_recipes():
    ret = []
    for recipe in db_recipes:
        populate_recipe(recipe)
        ret.append(recipe)
    ret.sort(key=lambda recipe: recipe["name"])
    return ret


def get_recipe(recipe_id):
    ret = db_recipes.find_one(id=recipe_id)
    if ret is None:
        return None
    populate_recipe(ret)
    return ret


def add_recipe(name, description, ingredients, reviews=None):
    db.begin()
    try:
        recipe_id = db_recipes.insert(dict(name=name, description=description))
        for ingredient in ingredients:
            db_ingredients.insert(dict(recipe=recipe_id, ingredient=ingredient))
        if reviews:
            for review in reviews:
                db_reviews.insert(dict(recipe=recipe_id, review=review))
        db.commit()
        return recipe_id
    except Exception as e:
        db.rollback()
        traceback.print_exc()


def add_review(recipe_id, review, author, rating):
    review_id = db_reviews.insert(dict(recipe=recipe_id, review=review, author=author, rating=rating))
    return review_id
