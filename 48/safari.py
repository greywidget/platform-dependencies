from itertools import cycle
import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def create_chart():
    cur_date, prev_date = None, None
    report = False
    line_type = cycle(["book", "status"])

    f = open(SAFARI_LOGS)
    while line := f.readline():
        if next(line_type) == "book":
            out_char = PY_BOOK if "python" in line.lower() else OTHER_BOOK
            report = False
        else:
            report = "sending" in line.lower()

        if report:
            cur_date = line[:5]
            if not cur_date == prev_date:
                print(f"\n{cur_date} ", end="")
                prev_date = cur_date
            print(out_char, end="")

    f.close()
