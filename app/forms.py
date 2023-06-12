from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField
from wtforms.validators import DataRequired

class ProfessorForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    materia = StringField('materia', validators=[DataRequired()])
    submit = SubmitField('cadastrar')

class AlunoForm(FlaskForm):
    cpf = StringField('cpf', validators=[DataRequired()])
    data_nascimento = DateField('data_nascimento', validators=[DataRequired()])
    sexo = StringField('sexo', validators=[DataRequired()])
    idade = FloatField('idade', validators=[DataRequired()])
    av1 = FloatField('av1', validators=[DataRequired()])
    av2 = FloatField('av2', validators=[DataRequired()])
    media = FloatField('media', validators=[DataRequired()])
    submit = SubmitField('cadastrar')
