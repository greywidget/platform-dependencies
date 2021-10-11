from collections import defaultdict
import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):
    counts = defaultdict(int)

    if not 5 < len(password) < 13:
        return False

    if password in used_passwords:
        return False

    for char in password:
        if char in string.digits:
            counts["digits"] += 1
        elif char in string.ascii_lowercase:
            counts["lowercase"] += 1
        elif char in string.ascii_uppercase:
            counts["uppercase"] += 1
        elif char in PUNCTUATION_CHARS:
            counts["punctuation"] += 1

    if (
        counts["digits"] < 1
        or counts["lowercase"] < 2
        or counts["uppercase"] < 1
        or counts["punctuation"] < 1
    ):
        return False

    used_passwords.add(password)
    return True
