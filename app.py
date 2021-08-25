import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    tutorials = list(mongo.db.tutorials.find())
    coaches = list(mongo.db.coaches.find())
    components = list(mongo.db.components.find())
    
    return render_template("home.html", tutorials=tutorials, coaches=coaches, components=components)


@app.route("/get_tutorials")
def get_tutorials():
    tutorials = list(mongo.db.tutorials.find())
    coaches = list(mongo.db.coaches.find())
    components = list(mongo.db.components.find())
    return render_template("tutorials.html", tutorials=tutorials, coaches=coaches, components=components)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username name already exists")
            return redirect(url_for("register"))

        password1 = request.form.get("password")
        password2 = request.form.get("confirm-password")

        if password1 != password2:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if user exists in 'sim_setup_world / users' database (MongoDB)
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches password in database
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # if password does not match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the database
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


@app.route("/submit_setup", methods=["GET", "POST"])
def submit_setup():
    if request.method == "POST":
        chosen_sim = request.form.get("sim_name")
        console.log(chosen_sim)
        chosen_car = request.form.get("car_name")
        console.log(chosen_car)
        chosen_track = request.form.get("track_name")
        console.log(chosen_track)
        if chosen_track != "" and chosen_sim == "":
            flash("Please choose a 'Sim' option")
        elif chosen_track != "" and chosen_car == "":
            flash("Please choose a 'Car' option")
        elif chosen_car != "" and chosen_sim == "":
            flash("Please choose a 'Sim' option")
        else:
            flash("This kind of worked!")
    sims = list(mongo.db.sims.find().sort("sim_name"))
    cars = list(mongo.db.car_list.find().sort("car_name"))
    tracks = list(mongo.db.tracks.find().sort("track_name"))
    return render_template(
        "submit_setup.html", sims=sims, cars=cars, tracks=tracks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
