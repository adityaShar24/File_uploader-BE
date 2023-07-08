import datetime
from flask import request , make_response
import json
from models.user_model import User
import bson.json_util as json_util
from flask_jwt_extended import create_access_token

def register():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    users = User(username= username , password= password)
    saved_users = users.save_users()
    json_Version = json_util.dumps(saved_users)
    return make_response({'message':'User registered successfully' , 'user': json_Version} , 201)

def login():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    access_token = create_access_token(identity= username + password , fresh=datetime.timedelta(minutes=15) )
    return make_response({'access_token': access_token} , 201)