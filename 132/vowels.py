VOWELS = list("aeiou")


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
    Return a tuple of the matching word and the vowel count, e.g.
    ('object-oriented', 6)"""
    last_word = None
    last_count = 0

    for word in text.strip().split():
        vowel_count = 0
        word = word.lower()
        for letter in word:
            if letter in VOWELS:
                vowel_count += 1
        if vowel_count > last_count:
            last_word = word
            last_count = vowel_count

    return last_word, last_count
