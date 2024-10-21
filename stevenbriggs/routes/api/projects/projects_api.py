from sqlalchemy import func

from stevenbriggs.app import db, Project


def create_project(project_json):
    """
    JSON KEYS:
    | title:         String (64)
    | repo_link:     String (256)
    | live_link:     String (256)
    | description:   String (8192)
    | img_filename:  String (128)
    
    -> Project
    """

    project = Project(title=title, repo_link=repo_link, repo_link_description=repo_link_description,
                      live_link=live_link, live_link_description=live_link_description,
                      short_description=short_description, description=description,
                      img_filename=img_filename)

    db.session.add(project)
    db.session.commit()

    return project


def get_project(project_id):
    """
    Gets a single project from the database specified by the project_id

    Parameters:
    ===========
    project_id: int

    -> Project or None
    """

    project = Project.query.filter_by(id=project_id).first()

    return project


def get_project_by_name(project_name):
    """
    Gets a single project from the database specified by the project_id

    Parameters:
    ===========
    project_id: int

    -> Project or None
    """

    project = Project.query.filter_by(title=project_name).first()

    return project


def get_all():
    """
    Creates a multi project object that has all the projects in the database

    -> project(s) JSON
    """
    projects = Project.query.all()
    print(projects)
    return projects


def random_project():
    """
    Gets a random Project from the database

    -> Project
    """

    return Project.query.order_by(func.random()).first()
