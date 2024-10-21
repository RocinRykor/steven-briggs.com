from flask import request, Blueprint
from flask_login import login_required

from stevenbriggs.routes.api.projects import projects_api

project_api = Blueprint("projects_api", __name__, url_prefix="/api/project")


@login_required
@project_api.route("/create/", methods=["POST"])
def create_project():
    """
    Method: POST

    Creates a project from the POSTed data

    Data must be in JSON format

    KEYS REQUIRED:
    ==============
    filename

    -> JSON Dict
    """

    project = projects_api.create_project(request.json)
    return project.jsonify(), 200


@project_api.route("/", methods=["GET"])
@project_api.route("/random/", methods=["GET"])
def random_project():
    return projects_api.random_project().jsonify(), 200


@project_api.route("/<int:project_id>", methods=["GET"])
def get_project(project_id):
    project = projects_api.get_project(project_id)

    if not project:
        return {"message": "project not found", "error": 404}, 200
    return project.jsonify()


@project_api.route("/all", methods=["GET"])
def get_all_projects():
    projects = projects_api.get_all()

    print(projects)

    projects = [project.jsonify() for project in projects]
    return projects
