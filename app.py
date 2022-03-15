from flask import Flask
from admin.Admin import start_views
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


# Método para receber as configurações e ciar o app
def create_app(config):
    app = Flask(__name__)
    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # True em produção
    
    app.config['FLASK_ADMIN_SWATCH'] = 'paper' # admin
    db = SQLAlchemy(app)

    start_views(app, db) # Admin
    Bootstrap(app) # Admin

    db.init_app(app)  # Database
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
