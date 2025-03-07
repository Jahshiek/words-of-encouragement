# from config import db



# class Portal(db.Model):
#     id = db.Column(db.Integer, primary_key=True) 
#     name = db.Column(db.String(100), default="General Feed", unique=True, nullable=False)
#     messages = db.relationship("Message", backref="portal", lazy=True)