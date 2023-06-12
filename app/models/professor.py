from app import db
import bcrypt

class Professor(db.Model):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    senha_hashed = db.Column(db.String(100))
    materia = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, senha, materia):
        self.nome = nome
        self.senha = senha
        self.materia = materia

    def set_password(self, password):
        self.senha_hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.senha_hashed)
    
    def save(self):
        with db.session.no_autoflush:
            db.session.add(self)
            db.session.commit()