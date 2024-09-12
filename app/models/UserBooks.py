from app import db


class UserBooks(db.Model):
    __tablename__ = "user_books"

    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )
    book_id = db.Column(
        db.Integer, db.ForeignKey("book.id", ondelete="CASCADE"), primary_key=True
    )

    def __repr__(self) -> str:
        return f"<UserBooks user_id: {self.user_id}, book_id: {self.book_id}>"
