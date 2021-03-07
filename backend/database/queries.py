create_parent_query = """
    CREATE TABLE IF NOT EXISTS parents (
        parent_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        mail TEXT NOT NULL,
        telephone TEXT
    )
    """

insert_parent_query = "INSERT INTO parents VALUES(?,?,?,?,?)"

create_kid_query = """
    CREATE TABLE IF NOT EXISTS kids (
        kid_id INTEGER PRIMARY KEY,
        parent INTEGER,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birthday TEXT NOT NULL,
        FOREIGN KEY(parent) REFERENCES parents(parent_id)
    )
    """

insert_kid_query = "INSERT INTO kids VALUES(?,?,?,?,?)"

create_user_query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        mail TEXT NOT NULL,
        role TEXT NOT NULL,
        hashed_password TEXT NOT NULL
    )
    """

insert_user_query = "INSERT INTO users VALUES(?, ?, ?, ?, ?)"

get_user_query = "SELECT * FROM users WHERE username = ?"