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
        return render_template("profile.html", page_title="Profile", username=username)

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


@app.route("/single_recipe")
def single_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "cost": request.form.get("cost"),
            "category_name": request.form.get("category_name"),
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
        flash("Your Recipe Was Successfully Added")
        return redirect(url_for("single_recipe"))

    return render_template("single_recipe.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
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
            "tools": request.form.get("tools"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for('group_recipes'))

    categories = mongo.db.categories.find().sort("category_name", 1)
    servings = mongo.db.servings.find().sort("serving_size", 1)
    leftovers = mongo.db.leftovers.find().sort("leftover_days", 1)
    prep_times = mongo.db.prep_times.find().sort("prep_time", 1)
    cook_times = mongo.db.cook_times.find().sort("cook_time", 1)
    tools = mongo.db.tools.find().sort("tools", 1)
    recipes = mongo.db.add_recipe.recipes.find().sort("recipe_name", 1)
    return render_template(
        "add_recipe.html", categories=categories,
        servings=servings, leftovers=leftovers,
        prep_times=prep_times, cook_times=cook_times, tools=tools, recipes=recipes)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
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
    mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
    flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    servings = mongo.db.servings.find().sort("serving_size", 1)
    leftovers = mongo.db.leftovers.find().sort("leftover_days", 1)
    prep_times = mongo.db.prep_times.find().sort("prep_time", 1)
    cook_times = mongo.db.cook_times.find().sort("cook_time", 1)
    tools = mongo.db.tools.find().sort("tools", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories,
        servings=servings, leftovers=leftovers,
        prep_times=prep_times, cook_times=cook_times, tools=tools)


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you! {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us")


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
        mongo.db.tasks.insert_one(recipe)
        flash("Task Successfully Added")
        return redirect(url_for("your_recipes"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    servings = mongo.db.servings.find().sort("serving_size", 1)
    leftovers = mongo.db.leftovers.find().sort("leftover_days", 1)
    prep_times = mongo.db.prep_times.find().sort("prep_time", 1)
    cook_times = mongo.db.cook_times.find().sort("cook_time", 1)
    tools = mongo.db.tools.find().sort("tools", 1)
    return render_template(
        "your_recipes.html", page_title="Your_Recipes", categories=categories, 
        servings=servings, leftovers=leftovers, 
        prep_times=prep_times, cook_times=cook_times, tools=tools)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)