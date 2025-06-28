from flask import Flask
from .models import Base  # SQLAlchemy base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_cors import CORS

SessionLocal = None

def create_app(config_class):
    global db, SessionLocal
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)

    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    SessionLocal = scoped_session(sessionmaker(bind=engine))
    app.config["DB_ENGINE"] = engine
    app.config["SESSION_FACTORY"] = SessionLocal

    with app.app_context():
        Base.metadata.create_all(bind=engine)

    from .routes import register_tasklist_routes, register_task_routes
    register_tasklist_routes(app, app.config["SESSION_FACTORY"], "/api/")
    register_task_routes(app, app.config["SESSION_FACTORY"], "/api/")

    return app