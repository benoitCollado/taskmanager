import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models import Base
from ..models import Task, TaskList
from .. import create_app
from ..configapp import TestConfig

TEST_DB_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DB_URL)
SessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="session")
def app():
  app = create_app(TestConfig)
  yield app

@pytest.fixture(scope="module")
def db(app):
  engine = app.config["DB_ENGINE"]
  SessionLocal = app.config["SESSION_FACTORY"]
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)
  db = SessionLocal()
  yield db
  db.close()
  Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(app):
  app.config["TESTING"] = True
  with app.test_client() as client:
    yield client

  
