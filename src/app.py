from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\Siddharth\\Desktop\\File_Uploader'

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug= True)