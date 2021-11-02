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


@app.route("/group_recipes")
def group_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("group_recipes.html", recipes=recipes)


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
            "tools": request.form.getlist("tools"),
            "ingredients": request.form.getlist("ingredients"),
            "preparation": request.form.getlist("preparation"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(recipe)
        flash("Task Successfully Added")
        return redirect(url_for("single_recipe"))
    categories = mongo.db.categories.find().sort("category_name")
    servings = mongo.db.servings.find().sort("serving_size")
    leftovers = mongo.db.leftovers.find().sort("leftover_days")
    prep_times = mongo.db.prep_times.find().sort("prep_time")
    cook_times = mongo.db.cook_times.find().sort("cook_time")
    tools = mongo.db.tools.find().sort("tools")
    # ingredients = mongo.db.ingredients.find("ingredients")
    # preparation = mongo.db.ingredients.find("preparation")
    # created_by = mongo.db.created_by.find("created_by")
    return render_template(
        "add_recipe.html", categories=categories,
        servings=servings, leftovers=leftovers,
        prep_times=prep_times, cook_times=cook_times, tools=tools)
        # tools=tools, ingredients=ingredients,
        # preparation=preparation, created_by=created_by)


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you! {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower(),
            "email": request.form.get("email").lower()}
        )

        if existing_user:
            flash("User Name or Email already exists")
            return redirect(url_for("register"))
        # dictionary 'register'
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
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

    return render_template("login.html")


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


@app.route("/single_recipe")
def single_recipe():
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
        return redirect(url_for("single_recipe"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    servings = mongo.db.servings.find().sort("serving_size", 1)
    leftovers = mongo.db.leftovers.find().sort("leftover_days", 1)
    prep_times = mongo.db.prep_times.find().sort("prep_time", 1)
    cook_times = mongo.db.cook_times.find().sort("cook_time", 1)
    tools = mongo.db.tools.find().sort("tools", 1)
    return render_template(
        "single_recipe.html", categories=categories, 
        servings=servings, leftovers=leftovers, 
        prep_times=prep_times, cook_times=cook_times, tools=tools)

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
        "your_recipes.html", categories=categories, 
        servings=servings, leftovers=leftovers, 
        prep_times=prep_times, cook_times=cook_times, tools=tools)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)