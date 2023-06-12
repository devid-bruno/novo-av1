from flask import Blueprint, render_template, redirect, url_for
import mysql.connector
from app.config import DATABASE_CONFIG
from app.models.aluno import Aluno
from app.forms import AlunoForm
from app import db
from flask import flash


conn = mysql.connector.connect(**DATABASE_CONFIG)

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('/index')
def index():    
    alunos = Aluno.query.all()
    return render_template('alunos/index.html', alunos=alunos)


@aluno_bp.route('/cadastro', methods=['GET', 'POST'])
def create():
    form = AlunoForm()

    if form.validate_on_submit():
        cpf = form.cpf.data
        data_nascimento = form.data_nascimento.data
        sexo = form.sexo.data
        idade = form.idade.data
        av1 = form.av1.data
        av2 = form.av2.data
        media = form.media.data

        aluno = Aluno(cpf=cpf, data_nascimento=data_nascimento, sexo=sexo, idade=idade, av1=av1, av2=av2, media=media)
        aluno.save()

        return redirect(url_for('aluno.index'))
    
    return render_template('alunos/cadastro.html', form=form)  

@aluno_bp.route('/editar/<int:cpf>', methods=['GET', 'POST'])
def aluno_editar(cpf):
    aluno = Aluno.query.get(cpf)
    form = AlunoForm(obj=aluno)

    if form.validate_on_submit():
        form.populate_obj(aluno)
        db.session.commit()
        
        return redirect(url_for('aluno.index'))

    return render_template('alunos/editar.html', form=form, aluno=aluno, cpf=cpf)

@aluno_bp.route('/excluir/<int:cpf>', methods=['POST'])
def aluno_excluir(cpf):
    aluno = Aluno.query.get(cpf)

    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        flash('Aluno excluído com sucesso.', 'success')
    else:
        flash('Aluno não encontrado.', 'error')

    return redirect(url_for('aluno.index', ))
