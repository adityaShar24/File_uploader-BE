from flask import Blueprint
from controller.file_uploader_controller import file_upload , get_all_files

file_bp = Blueprint('file_bp' , __name__)

@file_bp.post('/upload')
def file_uplaoder_wrapper():
    return file_upload()

@file_bp.get('/all_files')
def get_all_files_wrapper():
    return get_all_files()