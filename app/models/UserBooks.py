from app import db


# class UserBooks(db.Model):
#     __tablename__ = "user_books"

#     user_id = db.Column(
#         db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
#     )
#     book_id = db.Column(
#         db.Integer, db.ForeignKey("book.id", ondelete="CASCADE"), primary_key=True
#     )

#     def __repr__(self) -> str:
#         return f"<UserBooks user_id: {self.user_id}, book_id: {self.book_id}>"

user_books = db.Table(
    "user_books",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE")),
    db.Column("book_id", db.Integer, db.ForeignKey("book.id", ondelete="CASCADE")),
)
