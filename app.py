from flask import Flask
# Método para receber as configurações e ciar o app
def create_app(config):
    app = Flask(__name__)
    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # True em produção

    config.APP = app


    @app.after_request
    def after_request(response): # Para API
        response.headers.add('Acess-Control-Allow-Origin', '*')
        response.headers.add('Acess-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Acess-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
        return response


    @app.route('/')
    def index():
        return 'oi'
