from typing import List
from dataclasses import dataclass


@dataclass
class Version:
    major: int
    minor: float


def _todict(reqs: str) -> dict:

    to_dict = {}
    for line in reqs.split():
        package, version = line.split("==")
        maj, min = version.split(".", maxsplit=1)
        to_dict[package] = Version(int(maj), float(min))

    return to_dict


def changed_dependencies(old_reqs: str, new_reqs: str) -> List[str]:
    """Compare old vs new requirement multiline strings
    and return a list of dependencies that have been upgraded
    (have a newer version)
    """
    old = _todict(old_reqs)
    new = _todict(new_reqs)
    new_deps = []
    for k, v in old.items():
        new_version = new[k]
        if (
            new_version.major > v.major
            or new_version.major == v.major
            and new_version.minor > v.minor
        ):
            new_deps.append(k)

    return new_deps
