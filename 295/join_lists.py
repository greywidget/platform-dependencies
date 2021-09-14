from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if lst_of_lst == []:
        return None

    result = []
    for count, lst in enumerate(lst_of_lst, start=1):
        if lst:
            for item in lst:
                result.append(item)
            if count < len(lst_of_lst):
                result.append(sep)
    return result
