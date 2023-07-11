from flask import  request , make_response
from models.file_uploader_model import File
import bson.json_util as json_util


def file_upload():
    file = request.files['file']
    
    if file:
        saved_file = File(file.filename).savefile(file.read())
        json_version = json_util.dumps(saved_file)
        return make_response({'message':'File uploaded succesfully' , 'file': json_version} , 201)
    
    return make_response({'message': 'Invalid file'} , 400)


def get_all_files():
    files = File.get_all_files()
    json_Version = json_util.dumps(files)
    return make_response(json_Version , 201)