def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
    its octal representation.

    In Unix you have user, group and other permissions,
    each can have read (r), write (w), and execute (x)
    permissions expressed by r, w and x.

    Each has a number:
    r = 4
    w = 2
    x = 1

    So this leads to the following input/ outputs examples:
    rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
    rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
    r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """
    _cvt = {"x": 1, "w": 2, "r": 4}
    n = len(rwx) // 3
    chunks = [rwx[i : i + n] for i in range(0, len(rwx), n)]
    ret = ""
    for chunk in chunks:
        octl = sum(_cvt.get(item, 0) for item in chunk)
        ret += str(octl)
    return ret
