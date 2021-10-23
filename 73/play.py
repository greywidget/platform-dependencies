"""
This was just a quick test I did to prove to myself that the syntax of
the function call of check() does indeed pass a generator
"""

names = ["craig", "anne", "woody"]


def check(item):
    print(type(item))
    print(max(item))


check(name for name in names)
