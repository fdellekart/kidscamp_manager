def get_parent_id(db_conn):
    result = db_conn.execute("SELECT COUNT(*) FROM parents;")
    return result.fetchall()[0][0] + 1


def get_all_parents(db_conn):
    result = db_conn.execute("SELECT * FROM parents")
    return result.fetchall()