from flask import  request , make_response, send_file
from database.mongo import fs , users_collection
from models.file_uploader_model import File
from models.user_model import User
import bson.json_util as json_util
from bson.objectid import ObjectId


def file_upload():
    file = request.files['file']
    userId = request.form['userId']
    if file:
        saved_file = File(file.filename).savefile(file)
        update_user = User.update_user(userId = userId ,fileId= saved_file , filename= file.filename)
        json_version = json_util.dumps(saved_file)
        return make_response({'message':'File uploaded succesfully' , 'file': json_version } , 201)
    
    return make_response({'message': 'Invalid file'} , 400)

def get_file(filename):
    file = fs.find_one({ "filename": filename })
    return send_file(file, mimetype="image/png")


def get_dp(userId , filename):
    user_file = users_collection.find_one({"_id": ObjectId(userId) , "filename": filename})
    print(user_file)
    file = fs.find_one({ "filename": filename })
    if file.filename == user_file['filename']:
        return send_file(file , mimetype="image/png")
    return make_response({"message":"No file found"} , 404)

def get_all_files():
    files = File.get_all_files()
    json_Version = json_util.dumps(files)
    return make_response(json_Version , 201)