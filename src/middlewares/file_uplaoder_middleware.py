from flask import  request , make_response

def file_upload_middleware():
    if 'file' not in request.files:
        return make_response({'message':'No file uploaded'} , 400)
        
    file = request.files['file']
    if file.filename == '':
        return make_response({'message':'No file selected'} , 400)