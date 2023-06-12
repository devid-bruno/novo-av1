from flask import Blueprint, render_template, redirect, url_for
from app.forms import ProfessorForm
from app.models.professor import Professor
import mysql.connector
from app.config import DATABASE_CONFIG
from app import db

conn = mysql.connector.connect(**DATABASE_CONFIG)
prof_bp = Blueprint('professores', __name__)

@prof_bp.route('/entrar')
def index():
    professores = Professor.query.all()
    return render_template('professores/index.html', professores=professores)

@prof_bp.route('/cadastro', methods=['GET', 'POST'])
def create():
    form = ProfessorForm()

    if form.validate_on_submit():
        nome = form.nome.data
        materia = form.materia.data
        senha = form.senha.data

        professor = Professor(nome=nome, materia=materia, senha=senha)
        professor.set_password(senha)
        professor.save()

        return redirect(url_for('entrar'))

    return render_template('professores/diretoria.html', form=form)


