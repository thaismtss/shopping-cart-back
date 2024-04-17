import os
from flask import Flask
from flask_cors import CORS
from routes import init_routes


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}})

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config["FLASK_APP"] = os.environ.get("FLASK_APP")
    app.config["CORS_HEADERS"] = "Content-Type"

    init_routes(app)

    return app
