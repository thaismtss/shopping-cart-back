import pytest
from app.init import create_app
from app.models import db


@pytest.fixture(scope="session", autouse=True)
def app():
    app = create_app("testing")
    print(app.config)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
