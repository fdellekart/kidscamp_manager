from passlib.context import CryptContext


from .queries import get_user_query, insert_user_query
from models.users import UserInDB


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def get_user(username: str, db_conn):
    result = db_conn.execute(get_user_query, (username,))
    user = result.fetchone()
    if user:
        return UserInDB(user_id=user[0], username=user[1], mail=user[2], role=user[3], hashed_password=user[4])


def get_user_id(db_conn):
    result = db_conn.execute("SELECT COUNT(*) FROM users;")
    return result.fetchall()[0][0] + 1


def add_user(username: str, password:str, mail: str, role:str, db_conn):
    hashed_password = get_password_hash(password)
    user_id = get_user_id(db_conn)
    user_to_insert = (user_id, username, mail, role, hashed_password)
    db_conn.execute(insert_user_query, user_to_insert)
    db_conn.commit()