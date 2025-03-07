# from config import db



# class Messages(db.Model):
#     id = db.Column(db.Integer, primary_key=True) 
#     user_id = db.Column(db.Integer, db.ForeignKey("id"), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     created_at = db.Column(db.DateTime, default=db.func.now())

#     user = db.relationship("User", backref="messages")
    