from flask import  request , make_response , send_file
from models.file_uploader_model import File
from models.user_model import User
import bson.json_util as json_util



def file_upload():
    file = request.files['file']
    userId = request.form['userId']
    if file:
        saved_file = File(file.filename).savefile(file)
        update_user = User.update_user(userId = userId ,fileId= saved_file , filename= file.filename)
        json_version = json_util.dumps(saved_file)
        return make_response({'message':'File uploaded succesfully' , 'file': json_version } , 201)
    
    return make_response({'message': 'Invalid file'} , 400)


def get_all_files():
    files = File.get_all_files()
    json_Version = json_util.dumps(files)
    return make_response(json_Version , 201)

def get_file(filename):
    file = fs.find_one({ "filename": filename })
    return send_file(file, mimetype="image/png")
