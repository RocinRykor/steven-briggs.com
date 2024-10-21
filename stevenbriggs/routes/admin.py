from flask import Blueprint

admin = Blueprint("admin", __name__)


@admin.route("/admin/")
def admin_index():
    return "<h1>This will be the admin page</h1>"
