def get_parent_id(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM parents;")
    return cursor.fetchall()[0][0] + 1


def get_all_parents(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM parents")
    return cursor.fetchall()