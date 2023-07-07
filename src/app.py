from flask import Flask
from routes.file_uplaoder_router import file_bp
from middlewares.file_uplaoder_middleware import file_upload_middleware

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\Siddharth\\Desktop\\File_Uploader'


app.before_request(file_upload_middleware)
app.register_blueprint(file_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug= True)