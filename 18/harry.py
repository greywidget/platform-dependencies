import os
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
        harrywords = []
        for line in f.readlines():
            for word in line.split():
                fword = "".join(
                    [char for char in word.strip().lower() if char.isalpha()]
                )
                if fword and fword not in stopwords:
                    harrywords.append(fword)
    counter = Counter(harrywords)
    return counter.most_common(1)[0]
