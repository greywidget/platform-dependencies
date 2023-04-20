import csv
import os
from pathlib import Path
import re
from urllib.request import urlretrieve
from operator import itemgetter

data = "https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv"
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / "bites.csv"
A_BITE = re.compile(r"Bite (\d+)")

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
    output in the Bite description.
    Return a list of Bite IDs (int or str values are fine) of the N
    most complex Bites.
    """
    with open(stats, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        data = []
        for row in reader:
            if (difficulty := row["Difficulty"]) != "None":
                m = A_BITE.match(row["Bite"])
                bite = m.group(1)
                data.append((bite, float(difficulty)))

    return [bite for bite, _ in sorted(data, key=itemgetter(1), reverse=True)][:N]


if __name__ == "__main__":
    res = get_most_complex_bites()
    print(res)
