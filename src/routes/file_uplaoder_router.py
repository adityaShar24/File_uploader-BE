from flask import Blueprint
from controller.file_uploader_controller import file_upload , get_all_files , get_file , get_dp

file_bp = Blueprint('file_bp' , __name__)

@file_bp.post('/upload')
def file_uploader_wrapper():
    return file_upload()

@file_bp.get('/files/<filename>')
def get_file_wrapper(filename):
    return get_file(filename)

@file_bp.get('/user_dp/<userId>/<filename>')
def get_dp_wrapper(userId, filename):
    return get_dp(userId, filename)

@file_bp.get('/all_files')
def get_all_files_wrapper():
    return get_all_files()