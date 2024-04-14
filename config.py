from os import environ, path

class Config:
    DEBUG = True
    DEVELOPMENT = False
    FLASK_APP = environ.get("FLASK_APP")
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True