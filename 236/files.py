import difflib
from pathlib import Path


def get_matching_files(directory: Path, filter_str: str) -> list:
    """Get all file names in "directory" and (case insensitive) match the ones
    that exactly match "filter_str"

    In case there is no exact match, return closely matching files.
    If there are no closely matching files either, return an empty list.
    (Return file names, not full paths).

    For example:

    d = Path('.')
    files in dir: bite1 test output

    get_matching_files(d, 'bite1') => ['bite1']
    get_matching_files(d, 'Bite') => ['bite1']
    get_matching_files(d, 'pybites') => ['bite1']
    get_matching_files(d, 'test') => ['test']
    get_matching_files(d, 'test2') => ['test']
    get_matching_files(d, 'output') => ['output']
    get_matching_files(d, 'o$tput') => ['output']
    get_matching_files(d, 'nonsense') => []
    """
    file_names = {
        file.name.lower(): file.name for file in directory.glob("*") if file.is_file()
    }
    if exact_match := file_names.get(filter_str):
        return [exact_match]

    return difflib.get_close_matches(filter_str, file_names.values())
