import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/group")
def group_recipes():
    return render_template("group_recipes.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/goals")
def goals():
    return render_template("goals.html")


@app.route("/recipe")
def add_recipe():
    return render_template("add_recipe.html")


@app.route("/recipes")
def your_recipes():
    return render_template("your_recipes.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

