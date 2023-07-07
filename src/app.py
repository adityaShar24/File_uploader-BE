from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug= True)