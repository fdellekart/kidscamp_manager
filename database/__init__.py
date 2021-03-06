import sqlite3


from envyaml import EnvYAML
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


env = EnvYAML()

engine = create_engine(
    env["database_host"], connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_conn():
    return SessionLocal().connection().connection
