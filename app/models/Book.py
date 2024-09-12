from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    cover = db.Column(db.BLOB, nullable=True)

    # IK "libraried" is not a real word but it does the job lol.
    libraried_by = db.relationship(
        "User", secondary="user_books", backref="library_books"
    )

    def __init__(self, title: str, cover: bytes) -> None:
        self.title = title
        self.cover = cover

    def __repr__(self) -> str:
        return f"<Book {self.id}, title: {self.title}>"

    def get_user_lib_count(self) -> int:
        return len(self.libraried_by)
