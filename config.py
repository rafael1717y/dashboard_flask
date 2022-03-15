import os

class Config():
    CSRF_ENABLE = True # inibir fraude no envio de forms no servidor
    SECRET = '#1223293838@hahshd992892128172718727777777778172'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') #caminho absoluto do arquivo em exec.
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    IP_HOST = '192.0.0.1'
    PORT_HOST = 8080
    URL_MAIN = ''
    SQLALCHEMY_DATABASE_URI = ''


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = '192.0.0.1'
    PORT_HOST = 8080
    URL_MAIN = ''
    SQLALCHEMY_DATABASE_URI = ''



app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig()
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'



# Caminho absoluto do arquivo em exec.
print("Arquivo config ->", os.path.abspath(__file__)) #C:\Users\rafae\Desktop\code\dashboard_flask\config.py
print("Diretório raiz ->", os.path.dirname(os.path.abspath(__file__))) #C:\Users\rafae\Desktop\code\dashboard_flask
print("Pasta dos templates->", os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))