from flask import render_template, redirect, Blueprint, request, flash
from flask_login import current_user
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from stevenbriggs import models
from stevenbriggs.app import db
from stevenbriggs.forms import LoginForm

User = models.User

auth = Blueprint("auth", __name__)


@auth.route("/login/", methods=["POST"])
def login():
    # Make sure the form validates
    form = LoginForm(request.form)
    if not form.validate():
        # flash("Invalid form data", "error")
        flash_form_errors(form, "error")
        return render_template("public/users/login.html", title="Admin Login",
                               form=form)

    # Get the form data
    username = form.username.data
    password = form.password.data

    # Try select a user
    user = User.query.filter_by(username=username).first()
    if not user:
        flash("Invalid user or password.", "error")
        return render_template("public/users/login.html", title="Admin Login",
                               form=form)

    # Check the password.
    if check_password_hash(user.password, password):
        login_user(user, remember=True)
        user.authenticated = True
        return redirect("/")

    flash("Invalid user or password.", "error")
    return render_template("public/users/login.html", title="Invalid Login",
                           form=form)


@auth.route("/login/", methods=["GET"])
def display_login():
    form = LoginForm()
    return render_template("public/users/login.html", title="Admin Login",
                           form=form)


@auth.route("/login-form/", methods=["GET"])
def display_login_modal():
    form = LoginForm()
    return render_template("public/users/partials/login_form.html", title="Admin Login",
                           form=form)


@auth.route("/logout/")
def logout():
    current_user.authenticated = False
    logout_user()
    db.session.commit()
    return redirect("/")
