from collections import namedtuple

"""
A bit more elegant than mine, the PyBites version defines a helper function
which builds a dictionary of username: user and then does a lookup in this.
"""

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


def _get_user(username):
    users = {user.name: user for user in USERS}
    return users.get(username)


def get_secret_token(username):
    user = _get_user(username)
    if not user:
        raise UserDoesNotExist

    if user.expired:
        raise UserAccessExpired

    if user.role != ADMIN:
        raise UserNoPermission

    return SECRET
