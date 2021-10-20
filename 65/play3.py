"""
More examples with generators, this one from:
https://lerner.co.il/2020/05/08/making-sense-of-generators-coroutines-and-yield-from-in-python/
"""

import random


def bad_service_chatbot():
    answers = [
        "We don't do that",
        "We will get back to you right away",
        "Your call is very important to us",
        "Sorry, my manager is unavailable",
    ]
    yield "Can I help you?"
    s = ""
    while True:
        if s is None:
            break
        s = yield random.choice(answers)


g = bad_service_chatbot()
resp = next(g)
print(resp)
resp = g.send("I want to complain")
print(resp)
resp = g.send("No, really. I want to complain.")
print(resp)
