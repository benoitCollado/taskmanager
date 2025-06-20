from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

DATABASE_URL = "sqlite:///backend_flask/databaseflask.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()