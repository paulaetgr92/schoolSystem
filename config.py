import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua-secret-key-padrao')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///school_dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///school_prod.db')

def create_app():
    app = Flask(__name__)

    # Escolhe qual configuração usar
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    return app
