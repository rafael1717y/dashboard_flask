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

    @app.route('/')
    def index():
        return 'oi'
