from typing import List, Tuple


from envyaml import EnvYAML


from queries import (
    create_kid_query,
    create_parent_query,
    insert_parent_query,
    insert_kid_query,
)


env = EnvYAML()


def get_parent_id(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM parents;")
    return cursor.fetchall()[0][0]


def get_kid_id(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM kids;")
    return cursor.fetchall()[0][0]


def add_applications(parent: tuple, kids: List[Tuple], db_conn):
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

    parent_id = get_parent_id(db_conn)
    parent = tuple([parent_id,].extend(parent))

    first_kid_id = get_kid_id(db_conn)
    kids = [
        tuple([first_kid_id + offset, parent_id].extend(kid))
        for offset, kid in zip(range(len(kids)), kids)
    ]

    cursor.execute(insert_parent_query, parent)
    cursor.executemany(insert_kid_query, kids)
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
