"""
More examples with generators, this one from:
https://lerner.co.il/2020/05/08/making-sense-of-generators-coroutines-and-yield-from-in-python/
"""

import random


def pl_sentence(sentence):
    output = []
    for one_word in sentence.split():
        if one_word[0] in "aeiou":
            output.append(one_word + "way")
        else:
            output.append(one_word[1:] + one_word[0] + "ay")
    return " ".join(output)


def pig_latin_translator():
    s = ""
    while True:
        s = yield pl_sentence(s)
        if s is None:
            break


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


def switchboard():
    while True:
        choice = yield "Send 1 for Pig Latin, 2 for Support"
        if choice == 1:
            yield from pig_latin_translator()
        elif choice == 2:
            yield from bad_service_chatbot()
        elif choice == 3:
            return
        else:
            print("Bad choice; please try again")


s = switchboard()
resp = next(s)
print(resp)
# prime it...
print(s.send(2))
print(s.send("Hi There"))
print(s.send("la la la"))
print(s.send(None))

s.send(1)
print(s.send("hello"))
print(s.send(None))

s.send(3)
