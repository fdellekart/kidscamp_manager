from typing import List


from envyaml import EnvYAML


env = EnvYAML()


def resolve_apllicaton(data: dict) -> dict, List[dict]:
    """Extracts parent and kids from dict as it comes from Domainfactory POST
    Keys of data in dict from DF are specified in env.yaml
    Only appends kid to list of kids if name is not empty

    :param data: dict with keys as specified in env.yaml
    :return parent, kids: parent is dict with key name, mail, telephone
                            kids is list of dicts with keys name, birthday
    """
    parent = {
        name: data[env["parent_name"]],
        mail: data[env["mail"]],
        telephone: data[env["telephone"]],
    }
    kids = []
    for i in range(env["nr_of_kids"]):
        kid = {
            name: data[env[f"kid_{i}"]], 
            birthday: data[env[f"birthday_{i}"]]
        }
        if kid["name"]:
            kids.append(kid)
    return parent, kids