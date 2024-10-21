import json

from flask import render_template, Blueprint, request
from flask_login import login_required

from stevenbriggs.app import db, Project
from stevenbriggs.forms import ProjectForm
from stevenbriggs.utils import replace_markdown
import os

project = Blueprint("project", __name__, url_prefix="/project")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECTS_FILE_PATH = os.path.join(PROJECT_ROOT, 'static', 'json', 'projects.json')


@project.route("/")
def projects():
    with open(PROJECTS_FILE_PATH) as f:
        projects_data = json.load(f)

    return render_template("public/projects/projects.html",
                           title="Steven's Projects",
                           projects=projects_data,
                           replace_func=replace_markdown)

@project.route("/<int:id>")
def project_details(id):
    with open(PROJECTS_FILE_PATH) as f:
        projects_data = json.load(f)

    for project in projects_data:
        if project['id'] == id:
            return render_template("public/projects/project_page.html",
                                   title=project['title'],
                                   project=project,
                                   replace_func=replace_markdown)

    return "Project not found."


@login_required
@project.route("/add", methods=["GET"])
def get_add_project():
    form = ProjectForm(request.form)
    return render_template("public/projects/add_project.html", form=form)


@login_required
@project.route("/add", methods=["POST"])
def finish_add_project():
    form = ProjectForm(request.form)

    title = form.title.data
    repo_link = form.repo_link.data
    repo_link_description = form.repo_link_description.data
    live_link = form.live_link.data
    live_link_description = form.live_link_description.data
    short_description = form.short_description.data
    description = form.description.data
    img_filename = form.img_filename.data

    project = Project(title=title, repo_link=repo_link, repo_link_description=repo_link_description,
                      live_link=live_link, live_link_description=live_link_description,
                      short_description=short_description, description=description,
                      img_filename=img_filename)

    db.session.add(project)
    db.session.commit()

    return projects()
