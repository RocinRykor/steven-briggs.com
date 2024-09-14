from flask import Flask, redirect

def build_app():
    app = Flask(__name__)
    # statistics.init_app(app, db, Request, check_user)

    with app.app_context():
        # Base Routes
        from .routes.general import general

        app.register_blueprint(general)
        print("done")

    return app


application = build_app()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
