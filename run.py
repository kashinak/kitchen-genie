import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# instance of Flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# / refers to the default route
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # if there is a match in database and existing_user is truthy, we will display flash message
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html", page_title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}!".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Login")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/group_recipes")
def group_recipes():
    # convert Mongo Cursor Object into a proper list by wrapping find() inside Python list()
    recipes = list(mongo.db.recipes.find())
    return render_template(
        "group_recipes.html", page_title="Group_Recipes", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template(
        "group_recipes.html", page_title="Group_Recipes", recipes=recipes)


@app.route("/your_recipes")
def your_recipes():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "category_name": request.form.get("category_name"),
            "cost": request.form.get("cost"),
            "serving_size": request.form.get("serving_size"),
            "leftover_days": request.form.get("leftover_days"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "tools": request.form.getlist("tools"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("your_recipes"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    servings = mongo.db.servings.find().sort("serving_size", 1)
    leftovers = mongo.db.leftovers.find().sort("leftover_days", 1)
    prep_times = mongo.db.prep_times.find().sort("prep_time", 1)
    cook_times = mongo.db.cook_times.find().sort("cook_time", 1)
    tools = mongo.db.tools.find().sort("tools", 1)
    return render_template(
        "your_recipes.html", page_title="Your Recipes", categories=categories, 
        servings=servings, leftovers=leftovers, 
        prep_times=prep_times, cook_times=cook_times, tools=tools)


@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):
    print(recipe_id)
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("single_recipe.html", page_title="Single_Recipe", recipe=recipe)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "image": request.form.get("image"),
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "category_name": request.form.get("category_name"),
            "cost": request.form.get("cost"),
            "serving_size": request.form.get("serving_size"),
            "leftover_days": request.form.get("leftover_days"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "tools": request.form.get("tools"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for('group_recipes'))

    image = mongo.db.recipes.find_one("image")
    categories = mongo.db.categories.find().sort("category_name", 1)
    servings = mongo.db.servings.find().sort("serving_size", 1)
    leftovers = mongo.db.leftovers.find().sort("leftover_days", 1)
    prep_times = mongo.db.prep_times.find().sort("prep_time", 1)
    cook_times = mongo.db.cook_times.find().sort("cook_time", 1)
    tools = mongo.db.tools.find().sort("tools", 1)
  
    return render_template(
        "add_recipe.html", categories=categories,
        servings=servings, leftovers=leftovers,
        prep_times=prep_times, cook_times=cook_times, 
        tools=tools, image=image, page_title="Add Recipe")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        revise = {
            "image": request.form.get("image"),
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "category_name": request.form.get("category_name"),
            "cost": request.form.get("cost"),
            "serving_size": request.form.get("serving_size"),
            "leftover_days": request.form.get("leftover_days"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "tools": request.form.get("tools"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, revise)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    image = mongo.db.recipes.find_one("image")
    categories = mongo.db.categories.find().sort("category_name", 1)
    servings = mongo.db.servings.find().sort("serving_size", 1)
    leftovers = mongo.db.leftovers.find().sort("leftover_days", 1)
    prep_times = mongo.db.prep_times.find().sort("prep_time", 1)
    cook_times = mongo.db.cook_times.find().sort("cook_time", 1)
    tools = mongo.db.tools.find().sort("tools", 1)
    ingredients = mongo.db.ingredients.find()
    return render_template("edit_recipe.html", recipe=recipe, image=image, categories=categories, 
        servings=servings, leftovers=leftovers, prep_times=prep_times,
        cook_times=cook_times, tools=tools, ingredients=ingredients, page_title="Edit Recipe")


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("group_recipes"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you! {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  