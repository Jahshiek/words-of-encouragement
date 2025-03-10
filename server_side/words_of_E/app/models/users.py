from config import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(80), unique=False, nullable=False) 
    # email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False, default='')
    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_json(self):
        return {
           'id':self.id,
           'username': self.username,
        }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

