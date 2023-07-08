from flask import request , make_response
import json
from models.user_model import User
import bson.json_util as json_util


def register():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    users = User(username= username , password= password)
    saved_users = users.save_users()
    json_Version = json_util.dumps(saved_users)
    return make_response({'message':'User registered successfully' , 'user': json_Version} , 201)
