from flask import render_template, Blueprint  # , redirect, session, request

general = Blueprint("general", __name__)


@general.app_errorhandler(404)
def custom_error_page(e):
    return render_template("public/error.html", title="404 - Page Not Found!")


@general.route("/")
def index():
    return render_template("public/index.html", title="Steven Briggs Portfolio Site")


@general.route("/about")
def about():
    return render_template("public/about.html", title="About Steven")


@general.route("/contact")
def contact():
    return render_template("public/contact.html", title="Contact Steven")


@general.route("/testing")
def testing():
    return render_template("public/testing.html", title="JavaScript Testing Grounds")
