from .queries import get_user_query, insert_user_query
from models.users import UserInDB
from auth import get_password_hash


def get_user(username: str, db_conn):
    with db_conn.cursor() as cursor:
        cursor.execute(get_user_query, username)
        user = cursor.fetch()
    if user:
        return UserInDB(*user)


def get_user_id(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    return cursor.fetchall()[0][0] + 1


def add_user(username: str, password:str, mail: str, role:str, db_conn):
    hashed_password = get_password_hash(password)
    user_id = get_user_id(db_conn)
    user_to_insert = (user_id, username, mail, role, hashed_password)
    with db_conn.cursor() as cursor:
        cursor.execute(insert_user_query, user_to_insert)