from flask import Blueprint, render_template, request, redirect, flash
from app.models import User
from app import db
from app.encryption import encrypt_password, decrypt_password

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        encrypted_password = encrypt_password(password)

        user = User(username=username, password=encrypted_password)
        db.session.add(user)
        db.session.commit()

        flash(f'User {username} registered successfully!', 'success')
        return redirect('/')
    
    return render_template('register.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

       
        user = User.query.filter_by(username=username).first()
        if user and decrypt_password(user.password) == password:
            flash(f'Welcome back, {username}!', 'success')
            return redirect('/')
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

