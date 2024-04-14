import os
from flask import Flask
from routes import init_routes

def create_app():
    app = Flask(__name__)

    app.config.SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config.FLASK_APP = os.environ.get('FLASK_APP')
    
    init_routes(app)

    return app