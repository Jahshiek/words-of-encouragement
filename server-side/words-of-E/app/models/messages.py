from config import db


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_name = db.Column(db.String(80), unique=False, nullable=False) 
    password = db.Column(db.String(255), nullable=False)  

    def to_json(self):
        return {
           'id':self.id,
           'user_name': self.user_name,
           'password': self.password
        }