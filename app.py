""" Main Application Subroutines """

from datetime import datetime
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
    """ Function to render Home Page """
    return render_template("home.html")


# get data to inject into 'Tutorials' page
@app.route("/get_tutorials")
def get_tutorials():
    """ Template to render Tutorials Page """
    tutorials = list(mongo.db.tutorials.find())
    coaches = list(mongo.db.coaches.find())
    components = list(mongo.db.components.find())
    return render_template("tutorials.html", tutorials=tutorials,
                           coaches=coaches, components=components)


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Function to render 'Register New User' Page """
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username name already exists")
            return redirect(url_for("register"))

        password1 = request.form.get("password")
        password2 = request.form.get("confirm-password")

        # check passwords match
        if password1 != password2:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        # insert new user into database
        register_details = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register_details)

        # put the new user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

        # display 'Register' page on screen
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Function to render Login Page """
    if request.method == "POST":
        # check if user exists in 'database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches password in database
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                session["admin"] = mongo.db.users.find_one(
                  {"username": session["user"]})["admin"]
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


# display the user's profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """ Function to render User Profile Page """
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ Template to render Logged Out Page """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/submit_setup_part1", methods=["GET", "POST"])
def submit_setup_part1():
    """ Function to render initial 'Submit Setup' page """
    try:
        if session["user"]:
            if request.method == "POST":
                # Take user's 'sim' selection and inject cars and tracks
                # relating to the sim in question for user to choose from.
                sim_name = request.form["sim_name"]
                print("150: Selected Sim: ", sim_name)
                cars = list(mongo.db.car_list.find(
                    {"sim_name": request.form.get("sim_name")})
                    .sort("car_name"))
                tracks = list(mongo.db.tracks.find(
                    {"sim_name": request.form.get(
                        "sim_name")}).sort("track_name"))
                print("180: Car and Track options lists loaded - user needs" +
                      "to select car and track")
                return render_template(
                    "submit_setup_part2.html",
                    sim_name=sim_name, cars=cars, tracks=tracks)

            # Render the 'Submit Setup' page and inject 'Sim' options for
            # user to select from
            sims = list(mongo.db.sims.find().sort("sim_name"))
            print("100: Select Sim")
            return render_template(
                "submit_setup_part1.html", sims=sims)

    # If user not logged in flash the following message
    except KeyError:
        flash("Please login to submit a setup")
        return redirect(url_for("home"))


# Submit car and track choices
@app.route("/submit_setup_part2", methods=["GET", "POST"])
def submit_setup_part2():
    """ Function to render Page 2 of the Submit Setup process """
    if request.method == "POST":
        sim_name = request.form.get("sim_name")
        print("210: Part 2: Sim Name is: ", sim_name)
        car_name = request.form.get("car_name")
        print("220: Part 2: Car Name is: ", car_name)
        track_name = request.form.get("track_name")
        print("230: Part 2: Track Name is: ", track_name)
        headers = list(mongo.db.sim_headings.find({"sim_name": sim_name})
                                            .sort("heading_number"))
        setup_parameters = list(mongo.db.sim_settings_parameters.find(
                           {"sim_name": sim_name}).sort("order_number"))

        # Once user has selected both a 'Car' and 'Track', render a page of
        # required parameters for the sim in question.
        if track_name and car_name:
            return render_template(
                "submit_setup_part3.html",
                sim_name=sim_name,
                car_name=car_name, track_name=track_name,
                setup_parameters=setup_parameters, headers=headers)
        else:
            flash("Please select both a 'Car Name' and a 'Track Name")
            cars = list(mongo.db.car_list.find(
                {"sim_name": request.form.get("sim_name")}).sort("car_name"))
            tracks = list(mongo.db.tracks.find(
                {"sim_name": request.form.get("sim_name")}).sort("track_name"))
            print("180: Car and Track options lists loaded - user needs" +
                  " to select car and track")
            return render_template(
                "submit_setup_part2.html", sim_name=sim_name, cars=cars,
                tracks=tracks)


# Submit Parameters page
@app.route("/submit_setup_part3", methods=["GET", "POST"])
def submit_setup_part3():
    """ Function to render Page 3 of the Submit Setup process """
    if request.method == "POST":
        # Take user's parameter inputs and save as a setup to the database.
        sim_name = request.form.get("sim_name")
        print("Part 3 : ", sim_name)
        car_name = request.form.get("car_name")
        print("Part 3 : ", car_name)
        track_name = request.form.get("track_name")
        print("Part 3 : ", track_name)
        param_dict_list = list(mongo.db.sim_settings_parameters.find(
                           {"sim_name": sim_name}).sort("order_number"))
        print("Part 3 Parameters : ", param_dict_list)
        print("Length of Parameters List is : ", len(param_dict_list))
        date_time_obj = datetime.now()
        # the following line of code borrowed from
        # "https://thispointer.com/
        # python-how-to-convert-datetime-object-to-string-using-datetime-strftime/"
        # to get the current date and time.
        timestamp_str = date_time_obj.strftime("%Y %m %d - %H:%M:%S")
        print('Current Timestamp : ', timestamp_str)

        # Create a dictionary from the user's parameter values
        setup_dict = {}
        for param_dict in param_dict_list:
            parameter_name = param_dict["param"]
            setup_dict[parameter_name] = request.form.get(parameter_name)
        setup_dict["sim_name"] = sim_name
        setup_dict["car_name"] = car_name
        setup_dict["track_name"] = track_name
        setup_dict["created_by"] = session["user"]
        setup_dict["date_created"] = timestamp_str

        # Save the dictionary to the database
        mongo.db.setups.insert_one(setup_dict)
        flash("Setup Successfully Submitted")
        return render_template("home.html")


# Initial 'My Setups' page
@app.route("/my_setups_part1/", methods=["GET", "POST"])
def my_setups_part1():
    """ Function to render Page 1 of the My Setups process """
    try:
        if session["user"]:
            if request.method == "POST":
                # Take user's choice of sim and retrieve relevant car and track
                # lists for the sim in question.
                sim_name = request.form["sim_name"]
                cars = list(mongo.db.car_list.find(
                    {"sim_name": request.form.get("sim_name")}).
                    sort("car_name"))
                tracks = list(mongo.db.tracks.find(
                    {"sim_name": request.form.get("sim_name")}).
                    sort("track_name"))
                # Inject relevant cars and tracks and render on page 2 for user
                # to select from.
                return render_template(
                    "my_setups_part2.html",
                    sim_name=sim_name, cars=cars, tracks=tracks)

            # Render initial 'User Setups' page, and inject 'Sim' list for
            # user to choose from if they to narrow down their choices.
            sims = list(mongo.db.sims.find().sort("sim_name"))

            # Get a list of all the user's setups to be placed at the
            # bottom of the page for selection without having to filter.
            user_setups = list(mongo.db.setups.find(
                {"created_by": session["user"]}).sort("_id"))
            return render_template(
                "my_setups_part1.html", sims=sims, user_setups=user_setups)

    # If user not logged in flash the following message
    except KeyError:
        flash("Please login to Edit or Delete a setup")
        return redirect(url_for("home"))


# 'My Setups' car and track selection.
@app.route("/my_setups_part2", methods=["GET", "POST"])
def my_setups_part2():
    """ Function to render Page 2 of the My Setups process """
    # Take user's choice of car and track and retrieve relevant
    # setups from the database.
    if request.method == "POST":
        sim_name = request.form.get("sim_name")
        car_name = request.form.get("car_name")
        track_name = request.form.get("track_name")
        user_setups = list(mongo.db.setups.find({"created_by": session["user"],
                           "sim_name": sim_name, "car_name": car_name,
                                                 "track_name": track_name})
                           .sort("_id"))

        # once car and track selected, inject selections to my_setups_page3.
        if track_name and car_name:
            return render_template(
                "my_setups_part3.html",
                sim_name=sim_name,
                car_name=car_name, track_name=track_name,
                user_setups=user_setups)


# Take variables injected from my_setups_page2 and generate filtered list.
@app.route("/my_setups_part3", methods=["GET", "POST"])
def my_setups_part3():
    """ Function to render Page 3 of the My Setups process """
    if request.method == "POST":
        # Render the list using the variables received from my_setup_part2.
        return render_template("my_setups_part3.html")


@app.route("/edit_setup/<setup_id>", methods=["GET", "POST"])
def edit_setup(setup_id):
    """ Function to render the Edit Setup page """
    try:
        if session["user"]:
            if request.method == "POST":
                # Create a Dictionary from the users edited inputs to submit
                # to the database
                sim_name = request.args.get('sim_name', None)
                car_name = request.args.get('car_name', None)
                track_name = request.args.get('track_name', None)
                param_dict_list = list(mongo.db.sim_settings_parameters.find(
                                {"sim_name": sim_name}).sort("order_number"))
                update_dict = {}
                date_time_obj = datetime.now()
                # the following line of code borrowed from
                # "https://thispointer.com/
                # python-how-to-convert-datetime-object-to-string-using-datetime-strftime/"
                # to get the current date and time.
                timestamp_str = date_time_obj.strftime("%Y %m %d - %H:%M:%S")
                print('Current Timestamp PT6 : ', timestamp_str)
                for param_dict in param_dict_list:
                    parameter_name = param_dict["param"]
                    update_dict[parameter_name] = request.form.get(
                        parameter_name)
                update_dict["sim_name"] = sim_name
                update_dict["car_name"] = car_name
                update_dict["track_name"] = track_name
                update_dict["created_by"] = session["user"]
                update_dict["date_created"] = timestamp_str
                # Save the Dictionary of edited data to the Database
                mongo.db.setups.update({"_id": ObjectId(setup_id)},
                                       update_dict)
                flash("Setup Successfully Updated")
                return redirect(url_for("home"))

            # Load the 'Edit Setup' page creating a list of the user's own
            # setups at the bottom of the page.
            setup = mongo.db.setups.find_one({"_id": ObjectId(setup_id)})
            sim_name = setup["sim_name"]
            headers = list(mongo.db.sim_headings.find({"sim_name": sim_name})
                           .sort("heading_number"))
            setup_parameters = list(mongo.db.sim_settings_parameters.find(
                                {"sim_name": sim_name}).sort("order_number"))
            return render_template("edit_setup.html",
                                   setup=setup, headers=headers,
                                   setup_parameters=setup_parameters)

    # If user not logged in flas the following message
    except KeyError:
        flash("Please login to edit your setups")
        return redirect(url_for("home"))


@app.route("/view_setup/<setup_id>", methods=["GET", "POST"])
def view_setup(setup_id):
    """ Function to render the View Setup page """
    # Find the chosen setup using the Setup Id number and render to the screen
    # using the relevant headers and paramters for the sim concerned.
    setup = mongo.db.setups.find_one({"_id": ObjectId(setup_id)})
    sim_name = setup["sim_name"]
    headers = list(mongo.db.sim_headings.find({"sim_name": sim_name})
                   .sort("heading_number"))
    setup_parameters = list(mongo.db.sim_settings_parameters.find(
                           {"sim_name": sim_name}).sort("order_number"))
    return render_template("view_setup.html",
                           setup=setup, headers=headers,
                           setup_parameters=setup_parameters)


@app.route("/delete_setup/<setup_id>")
def delete_setup(setup_id):
    """ Function to render the Delete Setup page """
    # Delete the relevant setup denoted by the Setup ID number.
    mongo.db.setups.remove({"_id": ObjectId(setup_id)})
    flash("Setup Successfully Deleted")
    return redirect(url_for("my_setups_part1"))


@app.route("/find_setups_part1/", methods=["GET", "POST"])
def find_setups_part1():
    """ Function to render Page 1 of the Find Setups process """
    # Take the user's choice of sim and load the relevant cars and tracks
    # for that sim.
    if request.method == "POST":
        sim_name = request.form["sim_name"]
        cars = list(mongo.db.car_list.find(
            {"sim_name": request.form.get("sim_name")}).sort("car_name"))
        tracks = list(mongo.db.tracks.find(
            {"sim_name": request.form.get("sim_name")}).sort("track_name"))
        return render_template(
            "find_setups_part2.html",
            sim_name=sim_name, cars=cars, tracks=tracks)

    # Render the initial 'Find Setup Page'
    sims = list(mongo.db.sims.find().sort("sim_name"))
    user_setups = list(mongo.db.setups.find()
                                      .sort("_id"))
    return render_template(
        "find_setups_part1.html", sims=sims, user_setups=user_setups)


@app.route("/find_setups_part2", methods=["GET", "POST"])
def find_setups_part2():
    """ Function to render Page 2 of the Find Setups process """
    # Take the user's sim, car and track choices and create a list of results.
    if request.method == "POST":
        sim_name = request.form.get("sim_name")
        car_name = request.form.get("car_name")
        track_name = request.form.get("track_name")
        user_setups = list(mongo.db.setups.find({"sim_name": sim_name,
                                                 "car_name": car_name,
                                                 "track_name": track_name})
                           .sort("_id"))
        # Render the resulting list of setups to the screen
        if track_name and car_name:
            return render_template(
                "find_setups_part3.html",
                sim_name=sim_name,
                car_name=car_name, track_name=track_name,
                user_setups=user_setups)


@app.route("/find_setups_part3", methods=["GET", "POST"])
def find_setups_part3():
    """ Function to render Page 3 of the Find Setups process """
    # Take users sim, car and track choices and create a filtered list
    # to display on screen
    if request.method == "POST":
        sim_name = request.form.get("sim_name")
        car_name = request.form.get("car_name")
        sims = list(mongo.db.sims.find().sort("sim_name"))
        user_setups = list(mongo.db.setups.find({"created_by": session["user"],
                           "sim_name": sim_name, "car_name": car_name})
                           .sort("_id"))
        # Render the filter list
        return render_template("find_setups_part3.html",
                               sims=sims, user_setups=user_setups)


@app.route("/admin_tasks", methods=["GET", "POST"])
def admin_tasks():
    """ Function to render the Admin Tasks page """
    # Check user has 'Admin Rights'. If so, load the 'Admin Tasks' page.
    admin_type = mongo.db.users.find_one(
      {"username": session["user"]})["admin"]
    if admin_type is True:
        flash("User is an Admin")
        return render_template("admin_tasks.html")
    # Flash the following message if user does not have Admin Rights
    else:
        flash("Please request 'Admin' rights in order to access this function")
        return redirect(url_for("home"))


# Allow Admin User to view, edit or delete any setup on the database.
# Part 1 : load Initial page and unfiltered setup list
@app.route("/manage_setups_part1/", methods=["GET", "POST"])
def manage_setups_part1():
    """ Function to render Page 1 of the 'Admin' Manage Setups process """
    if request.method == "POST":
        # If user selects a Sim to filter on, find relevant cars and tracks
        sim_name = request.form["sim_name"]
        cars = list(mongo.db.car_list.find(
            {"sim_name": request.form.get("sim_name")}).sort("car_name"))
        tracks = list(mongo.db.tracks.find(
            {"sim_name": request.form.get("sim_name")}).sort("track_name"))
        # Reload page to give user choice of cars and tracks for
        # the chosen sim.
        return render_template(
            "manage_setups_part2.html",
            sim_name=sim_name, cars=cars, tracks=tracks)

    admin_type = mongo.db.users.find_one(
      {"username": session["user"]})["admin"]
    if admin_type is True:
        flash("User is an Admin")
        sims = list(mongo.db.sims.find().sort("sim_name"))
        user_setups = list(mongo.db.setups.find().sort("_id"))
        return render_template(
            "manage_setups_part1.html", sims=sims, user_setups=user_setups)
    else:
        flash("Please request 'Admin' rights in order to access this function")
        return redirect(url_for("home"))


# Allow Admin User to view, edit or delete any setup on the database.
# Part 2:  Re-render page  with car and track lists.
@app.route("/manage_setups_part2", methods=["GET", "POST"])
def manage_setups_part2():
    """ Function to render Page 2 of the 'Admin' Manage Setups process """
    admin_type = mongo.db.users.find_one(
        {"username": session["user"]})["admin"]
    if admin_type is True:
        flash("User is an Admin")
        if request.method == "POST":
            # Once user has chosen car and track and has clicked 'Find Setups'
            # generate a filtered list and reload the page with the results.
            sim_name = request.form.get("sim_name")
            car_name = request.form.get("car_name")
            track_name = request.form.get("track_name")
            user_setups = list(mongo.db.setups.find(
                            {"sim_name": sim_name, "car_name": car_name})
                           .sort("_id"))
            if track_name and car_name:
                print("Ending Part 2 and starting Part 3")
                return render_template(
                    "manage_setups_part3.html",
                    sim_name=sim_name,
                    car_name=car_name, track_name=track_name,
                    user_setups=user_setups)
            else:
                flash("Please select both a 'Car Name' and a 'Track Name")

        # Render page with car and track selections
        cars = list(mongo.db.car_list.find(
            {"sim_name": request.form.get("sim_name")}).sort(
                "car_name"))
        tracks = list(mongo.db.tracks.find(
            {"sim_name": request.form.get("sim_name")}).sort(
                "track_name"))
        print("180: Car and Track options lists loaded - user needs" +
              " to select car and track")
        return render_template(
            "manage_setups_part2.html", sim_name=sim_name, cars=cars,
            tracks=tracks)

    else:
        flash("Please request 'Admin' rights in order to access" +
              "this function")
        return redirect(url_for("home"))


# Allow Admin User to view, edit or delete any setup on the database.
# Part 3: Render filtered list with view, edit and delete buttons.
@app.route("/manage_setups_part3", methods=["GET", "POST"])
def manage_setups_part3():
    """ Function to render Page 3 of the 'Admin' Manage Setups process """
    if request.method == "POST":
        print("Started Admin Part 3")
        admin_type = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
        if admin_type is True:
            sim_name = request.form.get("sim_name")
            car_name = request.form.get("car_name")
            track_name = request.form.get("track_name")
            sims = list(mongo.db.sims.find().sort("sim_name"))
            user_setups = list(mongo.db.setups.find(
                {"sim_name": sim_name,
                    "car_name": car_name, "track_name": track_name})
                    .sort("_id"))
            return render_template("manage_setups_part3.html",
                                   sims=sims, user_setups=user_setups)

    else:
        flash("Please request 'Admin' rights in order to access" +
              "this function")
        return redirect(url_for("home"))


# Allow 'Admin Rights' user to amend any setup in the database.
@app.route("/edit_setup_admin/<setup_id>", methods=["GET", "POST"])
def edit_setup_admin(setup_id):
    """ Function to allow an Admin to edit any setup in the database """
    admin_type = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
    if admin_type is True:
        if request.method == "POST":
            # Create a Dictionary from input field values on the
            # 'Edit Setup' page.
            sim_name = request.args.get('sim_name', None)
            car_name = request.args.get('car_name', None)
            track_name = request.args.get('track_name', None)
            author = request.args.get('author', None)
            param_dict_list = list(mongo.db.sim_settings_parameters.find(
                            {"sim_name": sim_name}).sort("order_number"))
            update_dict = {}
            date_time_obj = datetime.now()
            # the following line of code borrowed from
            # "https://thispointer.com/
            # python-how-to-convert-datetime-object-to-string-using-datetime-strftime/"
            # to get the current date and time.
            timestamp_str = date_time_obj.strftime("%Y %m %d - %H:%M:%S")
            # Save the dictionary to the database
            for param_dict in param_dict_list:
                parameter_name = param_dict["param"]
                update_dict[parameter_name] = request.form.get(parameter_name)
            update_dict["created_by"] = author
            update_dict["sim_name"] = sim_name
            update_dict["car_name"] = car_name
            update_dict["track_name"] = track_name
            update_dict["date_created"] = timestamp_str
            mongo.db.setups.update({"_id": ObjectId(setup_id)}, update_dict)
            flash("Setup Successfully Updated")
            return redirect(url_for("admin_tasks"))

        # Load the chosen setup on the the screen.
        setup = mongo.db.setups.find_one({"_id": ObjectId(setup_id)})
        sim_name = setup["sim_name"]
        headers = list(mongo.db.sim_headings.find({"sim_name": sim_name})
                                            .sort("heading_number"))
        setup_parameters = list(mongo.db.sim_settings_parameters.find(
                            {"sim_name": sim_name}).sort("order_number"))
        return render_template("edit_setup_admin.html",
                               setup=setup, headers=headers,
                               setup_parameters=setup_parameters)

    else:
        flash("Please request 'Admin' rights in order to access" +
              "this function")
        return redirect(url_for("home"))


# Allow 'Admin Rights' user to delete any setup in the database.
@app.route("/delete_setup_admin/<setup_id>")
def delete_setup_admin(setup_id):
    """ Function to allow an Admin to delete any setup in the database """
    admin_type = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
    if admin_type is True:
        mongo.db.setups.remove({"_id": ObjectId(setup_id)})
        flash("Setup Successfully Deleted")
        return redirect(url_for("admin_tasks"))


@app.route("/manage_users_delete", methods=["GET", "POST"])
def manage_users_delete():
    """ Function to allow an Admin to delete any user in the database """
    admin_type = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
    if admin_type is True:
        flash("User is an Admin")
        if request.method == "POST":
            # check if user exists in 'sim_setup_world / users'
            # database (ie. MongoDB)
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})
            print(existing_user)
            session["password"] = mongo.db.users.find_one(
                    {"username": session["user"]})["password"]

            if existing_user:
                # check hashed password matches Admin's password
                if check_password_hash(
                  session["password"], request.form.get("password")):
                    mongo.db.users.remove(existing_user)
                    flash("User deleted")
                    return redirect(url_for('admin_tasks'))

                else:
                    # if password does not match
                    flash("Incorrect username and/or password")
                    return redirect(url_for("manage_users_delete"))

            else:
                # username doesn't exist
                flash("Incorrect username and/or password")
                return redirect(url_for("manage_users_delete"))

        return render_template("manage_users_delete.html")

    else:
        flash("Please request 'Admin' rights in order to access this function")
        return redirect(url_for("home"))


@app.route("/manage_users_edit", methods=["GET", "POST"])
def manage_users_edit():
    """ Function to allow an Admin to select any user
        in the database for editing """
    admin_type = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
    if admin_type is True:
        flash("User is an Admin")
        if request.method == "POST":
            # check if user exists in 'sim_setup_world / users'
            # database (ie. MongoDB)
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})
            session["password"] = mongo.db.users.find_one(
                    {"username": session["user"]})["password"]

            if existing_user:
                # check hashed password matches Admin's password
                if check_password_hash(
                  session["password"], request.form.get("password")):
                    return render_template('edit_user.html',
                                           existing_user=existing_user)

                else:
                    # if password does not match
                    flash("Incorrect username and/or password")
                    return redirect(url_for("manage_users_edit"))

            else:
                # username doesn't exist
                flash("Incorrect username and/or password")
                return redirect(url_for("manage_users_edit"))

        return render_template("manage_users_edit.html")

    else:
        flash("Please request 'Admin' rights in order to access" +
              "this function")
        return redirect(url_for("home"))


# Allow 'Admin Rights' user to edit or delete users from the database.
@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    """ Function to allow an Admin to edit any user in the database """
    admin_type = mongo.db.users.find_one(
            {"username": session["user"]})["admin"]
    if admin_type is True:
        flash("User is an Admin")
        if request.method == "POST":
            # Details are amended on screen then saved to the database.
            updated_details = {
              "username": request.form.get("username").lower(),
              "password": generate_password_hash(request.form.get("password")),
              "admin": request.form.get("admin")
            }
            mongo.db.user.update({"_id": ObjectId(user_id)}, updated_details)
            flash("User Successfully Updated")
            return render_template("admin_tasks.html")

        # Load the page
        return render_template("edit_user.html")

    else:
        flash("Please request 'Admin' rights in order to access" +
              "this function")
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
