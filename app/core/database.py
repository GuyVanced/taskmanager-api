# database connecitons setup

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlite_db_name = "task.db"
sqlite_url = f"sqlite:///{sqlite_db_name}"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url,connect_args=connect_args)

session = sessionmaker(engine)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

    