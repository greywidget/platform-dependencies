"""
Clearly nicer than my solution although I did get close to this in a few ways:
1. I figured out that I needed to type check the items as my attempts to
   check for iterability failed since a string of length 1 is iterable...
2. I did try using yield so that I didn't have to merge into a master list, 
   but for some reason I couldn't get that to work.
"""


def flatten(list_of_lists):
    """Use recursion: if list or tuple call self = go one level deeper,
    if base case return it. Using yield (generator) for convenience"""
    for item in list_of_lists:
        if type(item) in (list, tuple):
            yield from flatten(item)
        else:
            yield item
