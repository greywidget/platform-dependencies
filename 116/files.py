import os
from pathlib import Path

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""

    return [
        item.name
        for item in Path(dirname).glob("*")
        if item.is_file and ((item.stat().st_size / ONE_KB) >= size_in_kb)
    ]
