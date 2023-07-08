from models.user_model import User
from flask import request , make_response
import json


def register_user_middleware():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    if not username:
        return make_response({'message':'please enter username'} , 400)
    
    if not password:
        return make_response({'message':'please enter password'} , 400)