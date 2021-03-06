from unicodedata import category
from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>Successfully logged out.</p>"

@auth.route("/sign-up")
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be grater than 3 characters", category="error")
        elif len(firstName) < 2:
            flash("Firstname must be grater than 1f characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 7:
            flash("Password is to short. Needs at least 7 characters", category="error")
        else:
            flash("Account created!", category="success")


    return render_template("sign_up.html")
