from flask import Blueprint
from controller.file_uploader_controller import file_upload

file_bp = Blueprint('file_bp' , __name__)

@file_bp.post('/upload')
def file_uplaoder_wrapper():
    return file_upload()

