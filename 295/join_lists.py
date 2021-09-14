from typing import List, Union
from functools import reduce


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if lst_of_lst == []:
        return None

    result = []
    for count, lst in enumerate(lst_of_lst, start=1):
        for item in lst:
            result.append(item)
        if count < len(lst_of_lst):
            result.append(sep)
    return result


# def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
#     if not lst_of_lst:
#         return None

#     return reduce(lambda x, y: x + [sep] + y, lst_of_lst)


# def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
#     def joiner(lst_of_lst, sep):
#         for idx, lst in enumerate(lst_of_lst):
#             yield from lst
#             if idx < len(lst_of_lst) - 1:
#                 yield sep

#     if not lst_of_lst:
#         return None
#     return list(joiner(lst_of_lst, sep))
