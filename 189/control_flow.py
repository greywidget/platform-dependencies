from typing import List
IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names:List[str]):
    count = 0
    digits = set(str(i) for i in range(10))
    for name in names:
        if count == MAX_NAMES or name.startswith(QUIT_CHAR):
            return
        if name.startswith(IGNORE_CHAR) or set(name) & digits:
            continue
        count += 1
        yield name
