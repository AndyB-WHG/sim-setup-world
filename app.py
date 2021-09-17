import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
from datetime import datetime


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    # tutorials = list(mongo.db.tutorials.find())
    # coaches = list(mongo.db.coaches.find())
    # components = list(mongo.db.components.find())
    return render_template("home.html")
    # , tutorials=tutorials, coaches=coaches, components=components)


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


@app.route("/submit_setup_part1", methods=["GET", "POST"])
def submit_setup_part1():
    if request.method == "POST":
        sim_name = request.form["sim_name"]
        print("150: Selected Sim: ", sim_name)
        cars = list(mongo.db.car_list.find(
            {"sim_name": request.form.get("sim_name")}).sort("car_name"))
        tracks = list(mongo.db.tracks.find(
            {"sim_name": request.form.get("sim_name")}).sort("track_name"))
        print("180: Car and Track options lists loaded - user needs to" +
              "select car and track")
        return render_template(
            "submit_setup_part2.html",
            sim_name=sim_name, cars=cars, tracks=tracks)

    sims = list(mongo.db.sims.find().sort("sim_name"))
    print("100: Select Sim")
    return render_template(
        "submit_setup_part1.html", sims=sims)


@app.route("/submit_setup_part2", methods=["GET", "POST"])
def submit_setup_part2():
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
        print("")
        print("Headers: ", headers)
        print("")
        print("Parameters: ", setup_parameters)
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


@app.route("/submit_setup_part3", methods=["GET", "POST"])
def submit_setup_part3():
    if request.method == "POST":
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
        setup_dict = {}
        dateTimeObj = datetime.now()
        # the following line of code borrowed from "https://thispointer.com/python-how-to-convert-datetime-object-to-string-using-datetime-strftime/"
        # to get the current date and time.
        timestampStr = dateTimeObj.strftime("%Y %m %d - %H:%M:%S")
        print('Current Timestamp : ', timestampStr)
        for param_dict in param_dict_list:
            parameter_name = param_dict["param"]
            setup_dict[parameter_name] = request.form.get(parameter_name)
        setup_dict["sim_name"] = sim_name
        setup_dict["car_name"] = car_name
        setup_dict["track_name"] = track_name
        setup_dict["created_by"] = session["user"]
        setup_dict["date_created"] = timestampStr
        print(timestampStr)
        mongo.db.setups.insert_one(setup_dict)
        flash("Setup Successfully Submitted")
        return render_template("home.html")


@app.route("/my_setups_part1/", methods=["GET", "POST"])
def my_setups_part1():
    if request.method == "POST":
        # if setup_id:
        #     setup = mongo.db.setups.find_one({"_id": ObjectId(setup_id)})
        # else:
        sim_name = request.form["sim_name"]
        print("150: Selected Sim: ", sim_name)
        cars = list(mongo.db.car_list.find(
            {"sim_name": request.form.get("sim_name")}).sort("car_name"))
        tracks = list(mongo.db.tracks.find(
            {"sim_name": request.form.get("sim_name")}).sort("track_name"))
        print("180: Car and Track options lists loaded - user needs to" +
            "select car and track")
        return render_template(
            "my_setups_part2.html",
            sim_name=sim_name, cars=cars, tracks=tracks)

    sims = list(mongo.db.sims.find().sort("sim_name"))
    user_setups = list(mongo.db.setups.find({"created_by": session["user"]})
                                      .sort("_id"))
    print("user_setups : ", user_setups)
    return render_template(
        "my_setups_part1.html", sims=sims, user_setups=user_setups)


@app.route("/my_setups_part2", methods=["GET", "POST"])
def my_setups_part2():
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
        print("")
        print("Headers: ", headers)
        print("")
        print("Parameters: ", setup_parameters)
        user_setups = list(mongo.db.setups.find({"created_by": session["user"],
                           "sim_name": sim_name, "car_name": car_name})
                           .sort("_id"))
        if track_name and car_name:
            return render_template(
                "my_setups_part3.html",
                sim_name=sim_name,
                car_name=car_name, track_name=track_name,
                user_setups=user_setups)


@app.route("/my_setups_part3", methods=["GET", "POST"])
def my_setups_part3():
    if request.method == "POST":
        sim_name = request.form.get("sim_name")
        print("Part 3 : ", sim_name)
        car_name = request.form.get("car_name")
        print("Part 3 : ", car_name)
        track_name = request.form.get("track_name")
        print("Part 3 : ", track_name)
        sims = list(mongo.db.sims.find().sort("sim_name"))
        user_setups = list(mongo.db.setups.find({"created_by": session["user"],
                           "sim_name": sim_name, "car_name": car_name})
                           .sort("_id"))
        print("user_setups : ", user_setups)
        return render_template("my_setups_part3.html",
                               sims=sims, user_setups=user_setups)


@app.route("/edit_setup/<setup_id>", methods=["GET", "POST"])
def edit_setup(setup_id):
    if request.method == "POST":
        sim_name = request.args.get('sim_name', None)
        car_name = request.args.get('car_name', None)
        track_name = request.args.get('track_name', None)
        print("Part 6 : ", sim_name)
        print("Part 6 : ", car_name)
        print("Part 6 : ", track_name)
        param_dict_list = list(mongo.db.sim_settings_parameters.find(
                           {"sim_name": sim_name}).sort("order_number"))
        print("Part 6 Parameters : ", param_dict_list)
        print("Length of Parameters List is : ", len(param_dict_list))
        update_dict = {}
        dateTimeObj = datetime.now()
        # the following line of code borrowed from "https://thispointer.com/python-how-to-convert-datetime-object-to-string-using-datetime-strftime/"
        # to get the current date and time.
        timestampStr = dateTimeObj.strftime("%Y %m %d - %H:%M:%S")
        print('Current Timestamp PT6 : ', timestampStr)
        for param_dict in param_dict_list:
            parameter_name = param_dict["param"]
            update_dict[parameter_name] = request.form.get(parameter_name)
        update_dict["sim_name"] = sim_name
        update_dict["car_name"] = car_name
        update_dict["track_name"] = track_name
        update_dict["created_by"] = session["user"]
        update_dict["date_created"] = timestampStr
        print(timestampStr)
        mongo.db.setups.update({"_id": ObjectId(setup_id)}, update_dict)
        flash("Setup Successfully Updated")
        return redirect(url_for("home"))
    setup = mongo.db.setups.find_one({"_id": ObjectId(setup_id)})
    print("400 : Setup = : ", setup)
    sim_name = setup["sim_name"]
    print("410 : sim_name = : ", sim_name)
    headers = list(mongo.db.sim_headings.find({"sim_name": sim_name})
                   .sort("heading_number"))
    setup_parameters = list(mongo.db.sim_settings_parameters.find(
                           {"sim_name": sim_name}).sort("order_number"))
    return render_template("edit_setup.html",
                           setup=setup, headers=headers,
                           setup_parameters=setup_parameters)


@app.route("/view_setup/<setup_id>", methods=["GET", "POST"])
def view_setup(setup_id):
    setup = mongo.db.setups.find_one({"_id": ObjectId(setup_id)})
    print("500 : Setup = : ", setup)
    sim_name = setup["sim_name"]
    print("510 : sim_name = : ", sim_name)
    headers = list(mongo.db.sim_headings.find({"sim_name": sim_name})
                   .sort("heading_number"))
    setup_parameters = list(mongo.db.sim_settings_parameters.find(
                           {"sim_name": sim_name}).sort("order_number"))
    return render_template("view_setup.html",
                           setup=setup, headers=headers,
                           setup_parameters=setup_parameters)


@app.route("/delete_setup/<setup_id>")
def delete_setup(setup_id):
    print(setup_id)
    mongo.db.setups.remove({"_id": ObjectId(setup_id)})
    flash("Setup Successfully Deleted")
    # return render_template("home.html")
    return redirect(url_for("my_setups_part1"))


@app.route("/find_setups_part1/", methods=["GET", "POST"])
def find_setups_part1():
    if request.method == "POST":
        # if setup_id:
        #     setup = mongo.db.setups.find_one({"_id": ObjectId(setup_id)})
        # else:
        sim_name = request.form["sim_name"]
        print("150: Selected Sim: ", sim_name)
        cars = list(mongo.db.car_list.find(
            {"sim_name": request.form.get("sim_name")}).sort("car_name"))
        tracks = list(mongo.db.tracks.find(
            {"sim_name": request.form.get("sim_name")}).sort("track_name"))
        print("180: Car and Track options lists loaded - user needs to" +
            "select car and track")
        return render_template(
            "my_setups_part2.html",
            sim_name=sim_name, cars=cars, tracks=tracks)

    sims = list(mongo.db.sims.find().sort("sim_name"))
    user_setups = list(mongo.db.setups.find({"created_by": session["user"]})
                                      .sort("_id"))
    print("user_setups : ", user_setups)
    return render_template(
        "find_setups_part1.html", sims=sims, user_setups=user_setups)


@app.route("/find_setups_part2", methods=["GET", "POST"])
def find_setups_part2():
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
        print("")
        print("Headers: ", headers)
        print("")
        print("Parameters: ", setup_parameters)
        user_setups = list(mongo.db.setups.find({"created_by": session["user"],
                           "sim_name": sim_name, "car_name": car_name})
                           .sort("_id"))
        if track_name and car_name:
            return render_template(
                "find_setups_part3.html",
                sim_name=sim_name,
                car_name=car_name, track_name=track_name,
                user_setups=user_setups)


@app.route("/find_setups_part3", methods=["GET", "POST"])
def find_setups_part3():
    if request.method == "POST":
        sim_name = request.form.get("sim_name")
        print("Part 3 : ", sim_name)
        car_name = request.form.get("car_name")
        print("Part 3 : ", car_name)
        track_name = request.form.get("track_name")
        print("Part 3 : ", track_name)
        sims = list(mongo.db.sims.find().sort("sim_name"))
        user_setups = list(mongo.db.setups.find({"created_by": session["user"],
                           "sim_name": sim_name, "car_name": car_name})
                           .sort("_id"))
        print("user_setups : ", user_setups)
        return render_template("find_setups_part3.html",
                               sims=sims, user_setups=user_setups)


@app.route("/rate_setup/<setup_id>", methods=["GET", "POST"])
def rate_setup(setup_id):
    if request.method == "POST":
        print("900:  Rate Setup Id No:  ", setup_id)
        flash("'Rate Setup' awaiting coding. Id = " + setup_id)
        return redirect(url_for("find_setups_part1"))
    print("900:  Rate Setup Id No:  ", setup_id)
    flash("'Rate Setup' awaiting coding. Id = " + setup_id)
    return redirect(url_for("find_setups_part1"))


@app.route("/admin_tasks", methods=["GET", "POST"])
def admin_tasks():
    if request.method == "POST":
        print("1000 : Post Admin Task")
    admin_type = mongo.db.users.find_one(
      {"username": session["user"]})["admin"]
    if admin_type is True:
        flash("User is an Admin")
        return render_template("admin_tasks.html")
    else:
        flash("Please request 'Admin' rights in order to access this function")
        return redirect(url_for("home"))


@app.route("/add_sim", methods=["GET", "POST"])
def add_sim():
    admin_type = mongo.db.users.find_one(
      {"username": session["user"]})["admin"]
    if admin_type is True:
        flash("User is an Admin")
        if request.method == "POST":
            existing_sim = mongo.db.sims.find_one(
              {"sim_name": request.form.get("sim_name").lower()})
            if not existing_sim:
                for i in range(1, 21):
                    expected_header_name = "header" + str(i)
                    print("Expected Header Name : ", expected_header_name)
                    retrieved_header_name = request.form.get(
                        expected_header_name).lower()
                    print("Header Name typed by User : ", retrieved_header_name)
                    if retrieved_header_name:
                        if i < 10:
                            i *= 10
                            i = "0" + str(i)
                        elif i >= 10 and i < 100:
                            i = "0" + str(i)
                        header = {
                          "sim_name": request.form.get("sim_name").lower(),
                          "heading": retrieved_header_name,
                          "heading_number": i
                        }
                        mongo.db.sim_headings.insert_one(header)
                        flash("Sim submitted successfully")
                
        sims = list(mongo.db.sims.find().sort("sim_name"))
        print("1100: Displaying 'Add Sim' page")
        return render_template(
            "add_sim.html", sims=sims)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
