from controller.users_controller import register , login , get_all_users
from flask import Blueprint

auth_bp = Blueprint('auth_bp' , __name__)

@auth_bp.post('/register')
def register_wrapper():
    return register()

@auth_bp.post('/login')
def login_wrapper():
    return login()

@auth_bp.get('/all_users')
def get_all_users_wrapper():
    return get_all_users()