from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    make_response,
)
from flask_jwt_extended import jwt_required, create_access_token

from app.models.User import User
from app import db, jwt_manager

bp = Blueprint("auth", __name__, url_prefix="/auth")

jwt_manager.user_identity_loader


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        resp = make_response(redirect(url_for("home")))
        resp.set_cookie(
            "access_token",
            create_access_token(
                {"user_id": user.id, "username": user.username, "role": user.role}
            ),
            max_age=60 * 60 * 24 * 7,
            httponly=True,
        )
        return resp
    else:
        flash("Invalid username or password")
    return render_template("auth/login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/register.html")

    username = request.form.get("username")
    password = request.form.get("password")
    confirm = request.form.get("confirm")

    if password != confirm:
        flash("Passwords do not match")
        return render_template("auth/register.html")

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@bp.route("/logout")
@jwt_required()
def logout():
    resp = make_response(redirect(url_for("home")))
    resp.set_cookie("access_token", "", max_age=0, httponly=True)
    return resp
