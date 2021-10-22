from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()


def get_belt(user_score, scores=scores, belts=belts):
    from_score = scores[0::]
    to_score = scores[1::]
    mapper = OrderedDict(zip(zip(from_score, to_score), belts))
    if user_score < 10:
        return None
    elif user_score >= 1000:
        return belts[-1]

    for k, v in mapper.items():
        if k[0] <= user_score < k[1]:
            return v
