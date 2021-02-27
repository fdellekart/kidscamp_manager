from typing import List, Tuple


from envyaml import EnvYAML


from queries import (
    create_kid_query,
    create_parent_query,
    insert_parent_query,
    insert_kid_query,
)
from models.applications import Kid, Parent


env = EnvYAML()


def get_parent_id(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM parents;")
    return cursor.fetchall()[0][0] + 1


def get_kid_id(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM kids;")
    return cursor.fetchall()[0][0] + 1


def add_applications(parent: Parent, kids: List[Kid], db_conn):
    """Add parent to parents table and kids to kids table

    :param parent: (parent_id: int,
                    first_name: str,
                    last_name: str,
                    e_mail: str,
                    telephone: str)
    :param kids: list of tuples in form (kid_id: int,
                                         parent: int (id in parents table),
                                         first_name: str,
                                         last_name: str,
                                         birthday: str)
    :param db_conn: sqlite db connection
    """
    cursor = db_conn.cursor()

    cursor.execute(create_parent_query)
    cursor.execute(create_kid_query)

    parent.id = get_parent_id(db_conn)

    first_kid_id = get_kid_id(db_conn)
    for offset, kid in enumerate(kids):
        kid.id = first_kid_id + offset

    parent_to_insert = (
        parent.id,
        parent.first_name,
        parent.last_name,
        parent.mail,
        parent.telephone,
    )

    kid_to_insert = lambda kid: (
        kid.id,
        parent.id,
        kid.first_name,
        kid.last_name,
        kid.birthday,
    )
    kids_to_insert = [kid_to_insert(kid) for kid in kids]

    cursor.execute(insert_parent_query, parent_to_insert)
    cursor.executemany(insert_kid_query, kids_to_insert)
    db_conn.commit()


def get_all_kids(db_conn):
    """Get all kids in kids table

    :param db_conn: sqlite db connection
    :return: list of tuples in form (kid_id: int,
                                     parent: int (id in parents table),
                                     first_name: str,
                                     last_name: str)
    """
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM kids")
    return cursor.fetchall()


def get_all_parents(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM parents")
    return cursor.fetchall()
