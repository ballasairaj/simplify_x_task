import json

with open("policies/roles.json") as f:
    ROLES = json.load(f)

with open("policies/users.json") as f:
    USERS = json.load(f)


def get_user_permissions(username):

    role = USERS[username]

    return ROLES[role]


def filter_docs(username, docs):

    allowed = get_user_permissions(username)

    result = []

    for doc in docs:

        dept = doc.metadata.get(
            "department",
            "unknown"
        )

        if dept in allowed:

            result.append(doc)

    return result