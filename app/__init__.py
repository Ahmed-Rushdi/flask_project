from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(**kwargs):
    app = Flask(__name__)

    app.config.from_mapping(
        {
            "SECRET_KEY": "dev",
            "SQLALCHEMY_DATABASE_URI": "sqlite:///app.db",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )

    app.config.from_mapping(**kwargs)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
