from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.User import User

bp = Blueprint("users", __name__, url_prefix="/user")


@bp.route("/profile")
@jwt_required()
def profile():
    user_id = get_jwt_identity().get("user_id")
    user = User.query.get(user_id)
    if not user:
        return render_template("404.html"), 404
    return render_template("user/profile.html", user=user)
