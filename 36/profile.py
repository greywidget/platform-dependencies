def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError

    if len(sports) > 5:
        raise ValueError

    parms = {"name": name, "age": age}
    if sports:
        parms["sports"] = sorted([*sports])
    if awards:
        parms["awards"] = awards

    return parms
