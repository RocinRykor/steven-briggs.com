from flask import request, Blueprint
from flask_login import login_required

from stevenbriggs.routes.api.users import users_api

user_api = Blueprint("users_api", __name__, url_prefix="/api/user")


# @user_api.errorhandler(404)
# def not_found_error(e):
#     return {"error" : "Endpoint Not Found",
#     "status" : 404,
#     "message" : "The requested endpoint does not exist"}, 404

@login_required
@user_api.route("/create/", methods=["POST"])
def create_user():
    """
    Method: POST

    Creates a user from the POSTed data

    Data must be in JSON format

    KEYS REQUIRED:
    ==============
    name
    bio
    race
    gender
    status

    -> JSON Dict
    """

    user = users_api.create_user(request.json)
    return user.jsonify(), 200


@login_required
@user_api.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    """
    Method: POST

    While the method would be more clear if it was delete, sending a delete
    request from a web browser is nigh impossible in straight HTML forms.
    Using POST for simplicity.
    """

    user = users_api.delete_user(user_id)
    if not user:
        return None

    return {"message": "User Deleted"}, 200


@user_api.route("/edit/<int:user_id>", methods=["POST"])
def edit_user(quote_id):
    """
    Method: POST

    Edits the user with the title and user specified in the request json
    """

    user = users_api.edit_user(user_id, request.json)
    return user.jsonify(), 200


@user_api.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users_api.get_user(user_id)

    if not user:
        return {"message": "user not found", "error": 404}, 200
    return user.jsonify()


@user_api.route("/", methods=["GET"])
@user_api.route("/random/", methods=["GET"])
def random_user():
    return users_api.random_user().jsonify(), 200


@user_api.route("/all", methods=["GET"])
def get_all_users():
    users = users_api.get_all()
    users = [user.jsonify() for user in users]
    return users


@user_api.route("/limit/<int:user_limit>", methods=["GET"])
def get_multiple_users(user_limit):
    users = users_api.get_bulk(user_limit)
    users = [user.jsonify() for user in users]
    return users
