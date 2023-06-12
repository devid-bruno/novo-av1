from app import db 
from flask_login import UserMixin

class AuthProf(UserMixin, db.Model):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def check_password(self, password):
        return self.password == password