from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from init import create_app
from models import *

app = create_app()

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
