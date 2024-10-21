from flask import Flask, redirect
from flask_login import LoginManager
from flask_migrate import Migrate

from . import models
from .config import Config

db = models.db

# Create any items that will be used in the app
User = models.User
Project = models.Project

migrate = Migrate()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login/')


def build_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app, db)

    with app.app_context():
        # Base Routes
        from .routes.general import general
        from .routes.auth import auth
        from .routes.project import project

        app.register_blueprint(general)
        app.register_blueprint(auth)
        app.register_blueprint(project)

        # API Routes
        from .routes.api.projects.project_api_routes import project_api
        from .routes.api.users.user_api_routes import user_api

        app.register_blueprint(project_api)
        app.register_blueprint(user_api)

        print("Creating")
        db.create_all()
        print("done")

    return app


application = build_app()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
