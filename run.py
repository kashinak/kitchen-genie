import os
import json
from flask import Flask, render_template, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you! {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/login")
def login():
    return render_template("login.html", page_title="Log In")


@app.route("/register")
def register():
    return render_template("register.html", page_title="Register")


@app.route("/group")
def group_recipes():
    return render_template("group_recipes.html", page_title="Group Recipes")


@app.route("/profile")
def profile():
    return render_template("profile.html", page_title="Profile")


@app.route("/goals")
def goals():
    return render_template("goals.html", page_title="Goals")


@app.route("/recipe")
def add_recipe():
    return render_template("add_recipe.html", page_title="Add Recipe")


@app.route("/recipes")
def your_recipes():
    return render_template("your_recipes.html", page_title="Your Recipes")


@app.route("/logout")
def logout():
    return render_template("logout.html", page_title="Log Out")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
