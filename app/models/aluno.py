from app import db

class Aluno(db.Model):
    __tablename__ = 'aluno'

    cpf = db.Column(db.String(14), unique=True, primary_key=True)
    data_nascimento = db.Column(db.Date(), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    idade = db.Column(db.Integer(), nullable=False)
    av1 = db.Column(db.Float(), nullable=False)
    av2 = db.Column(db.Float(), nullable=False)
    media = db.Column(db.Float(), nullable=False)

    def __init__(self, cpf, data_nascimento, sexo, idade, av1, av2, media ):
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.idade = idade
        self.av1 = av1
        self.av2 = av2
        self.calcular_media()

    def calcular_media(self):
        if self.av1 is not None and self.av2 is not None:
            self.media = (self.av1 + self.av2) / 2
        else:
            self.media = None

    def save(self):
        db.session.add(self)
        db.session.commit()