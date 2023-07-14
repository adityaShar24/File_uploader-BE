from flask import Flask
from flask_jwt_extended import JWTManager
from routes.file_uploader_router import file_bp
from routes.user_router import auth_bp
from middlewares.file_uploader_middleware import file_upload_middleware
from middlewares.users_middeware import login_user_middleware , register_user_middleware

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\Siddharth\\Desktop\\File_Uploader'

JWTManager(app)
app.before_request(file_upload_middleware)
app.before_request(register_user_middleware)
app.before_request(login_user_middleware)
app.register_blueprint(file_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug= True)