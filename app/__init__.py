from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/faculdade'
    app.secret_key = 'secretkey'

    db.init_app(app)
    csrf = CSRFProtect(app)
    migrate = Migrate(app, db)

    from app.controllers.professoresController import prof_bp
    from app.controllers.alunoController import aluno_bp
    from app.controllers.authController import auth_bp

    app.register_blueprint(prof_bp, url_prefix='/professores/')
    app.register_blueprint(aluno_bp, url_prefix='/aluno/')
    app.register_blueprint(auth_bp, url_prefix='/')

    return app
