from flask import Blueprint, render_template, redirect, url_for, request
from functools import wraps
from flask import g, redirect, url_for, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('/professor/index'))

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login')) 
        return f(*args, **kwargs)
    return decorated_function