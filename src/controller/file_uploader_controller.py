from flask import  request , make_response
from models.file_uploader_model import File
from werkzeug.utils import secure_filename
import os
import bson.json_util as json_util
# from app import app


def file_upload():
    file = request.files['file']
    
    if file:
        filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        new_file = File(filename)
        saved_file = new_file.save_file()
        json_version = json_util.dumps(saved_file)
        return make_response({'message':'File uploaded succesfully' , 'file': json_version} , 201)
    
    return make_response({'message': 'Invalid file'} , 400)


def get_all_files():
    files = File.get_all_files()
    json_Version = json_util.dumps(files)
    return make_response(json_Version , 201)