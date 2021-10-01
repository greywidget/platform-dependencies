import os
import re
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def get_harry_most_common_word():
    with open(stopwords_file) as f:
        stopwords = [line.strip() for line in f.readlines()]

    with open(harry_text, encoding="utf-8") as f:
        # Use re to replace non alpha chars with nothing e.g strip them out
        words = [re.sub(r"\W+", r"", word) for word in f.read().lower().split()]
        words = [word for word in words if word.strip() and word not in stopwords]
        counter = Counter(words)
    return counter.most_common(1)[0]
