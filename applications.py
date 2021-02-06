from typing import List, Tuple
import os


from envyaml import EnvYAML
import pandas as pd

from queries import create_kid_query, create_parent_query, insert_parent_query, insert_kid_query


env = EnvYAML()


def resolve_application(data: dict):
    """Extracts parent and kids from dict as it comes from Domainfactory POST
    Keys of data in dict from DF are specified in env.yaml
    Only appends kid to list of kids if name is not empty

    :param data: dict with keys as specified in env.yaml
    :return parent, kids: parent is dict with key name, mail, telephone
                            kids is list of dicts with keys name, birthday
    """
    parent = {
        "name": data[env["parent_name"]],
        "mail": data[env["mail"]],
        "telephone": data[env["telephone"]],
    }
    kids = []
    for i in range(env["nr_of_kids"]):
        kid = {"name": data[env[f"kid_{i}"]], "birthday": data[env[f"birthday_{i}"]]}
        if kid["name"]:
            kids.append(kid)
    return parent, kids


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
