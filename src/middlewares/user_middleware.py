from models.user_model import User
from flask import request , make_response
import json


def register_user_middleware():
    if request.endpoint == 'auth_bp.register_wrapper':
        body = json.loads(request.data)
        username = body['username']
        password = body['password']
        if not username:
            return make_response({'message':'please enter username'} , 400)
        
        if not password:
            return make_response({'message':'please enter password'} , 400)
        existing_user = User.find_by_username(username)
        if existing_user:
            return make_response({'message':'username aleardy exists please enter unique username'} , 400)
    
    
def login_user_middleware():
    if request.endpoint == 'auth_bp.login_wrapper':
        body = json.loads(request.data)
        username = body['username']
        password = body['password']
        if not username:
            return make_response({'message':'please enter username'} , 400)
        
        if not password:
            return make_response({'message':'please enter password'} , 400)

        existing_user = User.find_by_username(username)
        if not existing_user:
            return make_response({'message':'cannot find user please enter username correctly'} , 400)