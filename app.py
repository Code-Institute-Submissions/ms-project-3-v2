import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# Import Werkzeug security helpers
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists! Please try again.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration complete!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and Password combination")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and Password combination")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been sucessfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "difficulty_level": request.form.get("difficulty_level"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "added_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        return redirect(url_for("get_recipes"))

    # wire-up data from Categories and Difficulty Levels collections on MongoDB
    categories = mongo.db.categories.find()
    difficulty_levels = mongo.db.difficulty_levels.find()
    return render_template(
            "add_recipe.html",
            categories=categories,
            difficulty_levels=difficulty_levels
        )


@app.route("/recipe_details/<recipe_id>")
def recipe_details(recipe_id):
    return render_template(
        "recipe_details.html", recipe=mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})
        )


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # allows user to edit recipe details
    if request.method == "POST":
        save_changes = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "difficulty_level": request.form.get("difficulty_level"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "added_by": session["user"]
        }
        mongo.db.recipes.replace_one(
            {"_id": ObjectId(recipe_id)}, save_changes
            )

    # retrieve recipe to be edited
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find()
    difficulty_levels = mongo.db.difficulty_levels.find()

    return render_template(
            "edit_recipe.html",
            recipe=recipe,
            categories=categories,
            difficulty_levels=difficulty_levels,
        )


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("The recipe was sucessfully deleted")
    return redirect(url_for("get_recipes"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
