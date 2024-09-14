from flask import render_template, Blueprint, request
import random

# from sixthworldsprawl.app import db, User, Character

general = Blueprint("general", __name__)

@general.app_errorhandler(404)
def custom_error_page(e):
    return render_template("public/error.html", title="404 - Page Not Found!")


@general.route("/")
@general.route("/index")
@general.route("/home")
def index():
    return render_template("public/index.html", title="Steven Briggs Contact/Portfolio")
