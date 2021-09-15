from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    for index, name in enumerate(names, start=1):
        print(f"| {name:<10}", end=None if index % cols == 0 else "")
