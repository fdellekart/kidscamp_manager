from typing import List
import os


from envyaml import EnvYAML
import pandas as pd


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


def add_applications(parent: dict, kids: List[dict]):
    path = f"{env['data_directory']}/{env['data_file']}"
    df_columns = ["name", "birthday", "parent_name", "mail", "telephone"]
    if os.path.isfile(path):
        data = pd.read_csv(path)
    else:
        data = pd.DataFrame(columns=df_columns)
    for kid in kids:
        application = pd.DataFrame(
            {
                "name": kid["name"],
                "birthday": kid["birthday"],
                "parent_name": parent["name"],
                "mail": parent["mail"],
                "telephone": parent["telephone"],
            },
            columns=df_columns,
            index=[
                1,
            ],
        )
        data = data.append(application, ignore_index=True)
    data.to_csv(path, index=False)


def get_all_applications():
    path = f"{env['data_directory']}/{env['data_file']}"
    if os.path.isfile(path):
        return pd.read_csv(path).to_dict("records")
