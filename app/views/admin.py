from flask import Blueprint, render_template


bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.route("/panel")
def panel():
    return render_template("admin/panel.html")


# TODO:
# - add user management
# - add book management
# - authorization
