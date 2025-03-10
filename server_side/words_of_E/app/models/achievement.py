# from config import db

# class Achievement(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     badge_name = db.Column(db.String(50), nullable=False)
#     timestamp = db.Column(db.DateTime, default=db.func.now())

#     user = db.relationship('User', backref=db.backref('achievements', lazy=True))
