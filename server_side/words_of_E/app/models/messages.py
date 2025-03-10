from config import db



class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship('User', backref=db.backref('messages', lazy=True))
    category = db.relationship('Category', backref=db.backref('messages', lazy=True))


# 2. Message Model
# Represents posts/messages in the feed.
# CRUD Operations:
# Create: Post a new message.
# Read: Fetch messages by category, user, or general feed.
# Update: Edit message content.
# Delete: Remove a message.

    