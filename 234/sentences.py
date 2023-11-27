import re

RE_SENTENCE = re.compile(r"[^.?!]+(\.|!|\?)\s*")


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
    in dot (.), question mark (?) and exclamation mark (!)"""
    sentences = [match.group().capitalize() for match in re.finditer(RE_SENTENCE, text)]
    return "".join(sentences)
