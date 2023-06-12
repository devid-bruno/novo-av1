from flask import Blueprint
import mysql.connector
from app.config import DATABASE_CONFIG

conn = mysql.connector.connect(**DATABASE_CONFIG)

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM professor')
    professores = cursor.fetchall()
    return professores

@home_bp.route('/alunos')
def alunos():
    return 'a'