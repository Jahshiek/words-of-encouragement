from config import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_name = db.Column(db.String(80), unique=False, nullable=False) 
    password_hash = db.Column(db.String(255), nullable=False)
    
    def to_json(self):
        return {
           'id':self.id,
           'user_name': self.user_name,
        }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
