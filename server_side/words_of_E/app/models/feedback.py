from config import db

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    feedback_type = db.Column(db.String(10), nullable=False)  # 'like' or 'comment'
    comment_text = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship('User', backref=db.backref('feedback', lazy=True))
    message = db.relationship('Message', backref=db.backref('feedback', lazy=True))
