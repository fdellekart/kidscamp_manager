def get_kid_id(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM kids;")
    return cursor.fetchall()[0][0] + 1


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