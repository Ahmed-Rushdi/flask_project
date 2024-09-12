from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.utils import bytes_to_base64
from datetime import timedelta


db = SQLAlchemy()
jwt_manager = JWTManager()


def create_app(**kwargs):
    app = Flask(__name__)

    app.config.from_mapping(
        {
            "SECRET_KEY": "dev",
            "SQLALCHEMY_DATABASE_URI": "sqlite:///app.db",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "JWT_SECRET_KEY": "dev",
            "JWT_ACCESS_TOKEN_EXPIRES": timedelta(minutes=30),
            "JWT_TOKEN_LOCATION": ["cookies"],
        }
    )
    app.config.from_mapping(**kwargs)
    app.jinja_env.filters["bytes_to_base64"] = bytes_to_base64

    jwt_manager.init_app(app)

    from app.models.User import User
    from app.models.Book import Book
    from app.models.UserBooks import user_books

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return render_template("layout.html")

    from app.views import auth, users, admin, books

    app.register_blueprint(auth.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(books.bp)

    # app.register_blueprint(views)

    return app
