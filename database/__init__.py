import sqlite3


def get_db_conn():
    db_conn = sqlite3.connect("kidscamp.db")
    try:
        yield db_conn
    finally:
        db_conn.close()