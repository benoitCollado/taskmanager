class Config : 
  SQLALCHEMY_DATABASE_URI = "sqlite:////home/runner/workspace/backend_flask/databaseflask.db"
  TESTTING = False

class TestConfig:
  SQLALCHEMY_DATABASE_URI = "sqlite:///backend_flask/testdatabase.db"
  TESTING = True