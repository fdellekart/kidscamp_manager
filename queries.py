create_parent_query = """
    CREATE TABLE IF NOT EXISTS parents (
        parent_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        e_mail TEXT NOT NULL,
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