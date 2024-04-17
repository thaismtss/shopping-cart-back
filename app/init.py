from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .routes import init_routes
from .models import db
from .config import config


def create_app(config_name="default"):
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "*"}})

    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate = Migrate(app, db)

    init_routes(app)

    return app
