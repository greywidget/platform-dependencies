"""
More examples with generators, this one from:
https://lerner.co.il/2020/05/08/making-sense-of-generators-coroutines-and-yield-from-in-python/
"""


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


g = pig_latin_translator()
next(g)
data = g.send("what on this earth are you on about?")
print(data)
