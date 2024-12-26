from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user
from . import db

auth = Blueprint('auth', __name__)

SECRET_KEY = "HFX@5971&"  # Secret key for admin access (store securely)

# Add this login route to your auth.py

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('views.home'))  # Redirect to the index or main page after login
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        secret_key = request.form.get('secret_key', '').strip()

        # Check if secret key is correct to assign admin status
        is_admin = secret_key == SECRET_KEY

        # Check if the email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already registered.', 'danger')
            return redirect(url_for('auth.register'))

        # Hash password before storing it
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create a new user
        new_user = User(email=email, password=hashed_password, first_name=first_name, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')