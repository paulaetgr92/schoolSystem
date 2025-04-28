import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Config:

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua-secret-key-padrao')

class DevelopmentConfig(Config):

    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

def create_app():
    from flask import Flask

    app = Flask(__name__)

    # Escolhe qual configuração usar
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    return app

