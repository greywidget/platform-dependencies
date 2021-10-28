def flatten(list_of_lists):

    master = []
    for item in list_of_lists:
        if isinstance(item, list) or isinstance(item, tuple):
            master.extend(flatten(item))
        else:
            master.append(item)

    return master
