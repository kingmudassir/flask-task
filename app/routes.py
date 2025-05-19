from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .models import db, User, Department, EmployeeProfile, LeaveRequest
from .auth import admin_required

api = Blueprint('api', __name__)

# Admin Routes
@api.route('/api/admin/employees', methods=['GET'])
@login_required
@admin_required
def list_employees():
    users = User.query.all()
    return jsonify([{'id': u.id, 'email': u.email} for u in users])

@api.route('/api/admin/employees', methods=['POST'])
@login_required
@admin_required
def add_employee():
    data = request.json
    hashed_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
    user = User(emp_id=data['emp_id'], email=data['email'], password_hash=hashed_pw,
                role=data['role'], department_id=data['department_id'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'User added'})

# Employee Routes
@api.route('/api/profile', methods=['GET'])
@login_required
def get_profile():
    profile = EmployeeProfile.query.filter_by(user_id=current_user.id).first()
    return jsonify({'full_name': profile.full_name, 'salary': profile.salary})

@api.route('/api/profile/contact', methods=['PATCH'])
@login_required
def update_contact():
    data = request.json
    profile = EmployeeProfile.query.filter_by(user_id=current_user.id).first()
    profile.contact = data['contact']
    db.session.commit()
    return jsonify({'msg': 'Contact updated'})

@api.route('/api/leave', methods=['POST'])
@login_required
def submit_leave():
    data = request.json
    leave = LeaveRequest(employee_id=current_user.id,
                         start_date=data['start_date'],
                         end_date=data['end_date'])
    db.session.add(leave)
    db.session.commit()
    return jsonify({'msg': 'Leave requested'})
