import pytest
from config import create_app
from model import db  # ajusta se o import for diferente

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    flask_app.config['TESTING'] = True

    db.init_app(flask_app)

    with flask_app.app_context():
        db.create_all()
        yield flask_app.test_client()
        db.drop_all()
