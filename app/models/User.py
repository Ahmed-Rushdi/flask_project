from app import db
import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), unique=False, nullable=False)
    role = db.Column(db.String(30), unique=False, nullable=False, default="user")
    avatar = db.Column(db.BLOB, nullable=True)
    books = db.relationship("Book", secondary="user_books", back_populates="users")

    def __init__(self, username: str, password: str, role: str = "user") -> None:
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self) -> str:
        return f"<User {self.id}, username: {self.username}>"

    @property
    def password(self) -> None:
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())
