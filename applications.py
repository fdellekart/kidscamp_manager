from typing import List, Tuple


from envyaml import EnvYAML


from queries import (
    create_kid_query,
    create_parent_query,
    insert_parent_query,
    insert_kid_query,
)


env = EnvYAML()


def add_applications(parent: tuple, kids: List[Tuple], db_conn):
    cursor = db_conn.cursor()

    cursor.execute(create_parent_query)
    cursor.execute(create_kid_query)

    cursor.execute(insert_parent_query, parent)
    cursor.executemany(insert_kid_query, kids)
    db_conn.commit()


def get_all_kids(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM kids")
    return cursor.fetchall()
