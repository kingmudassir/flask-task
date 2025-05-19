from flask import Blueprint, request, jsonify, session
from .models import User
from . import db, login_manager
from flask_login import login_user, logout_user, login_required
import bcrypt

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.checkpw(data['password'].encode(), user.password_hash.encode()):
        login_user(user)
        session.permanent = True
        return jsonify({"msg": "Logged in"})
    return jsonify({"msg": "Invalid credentials"}), 401

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"msg": "Logged out"})
