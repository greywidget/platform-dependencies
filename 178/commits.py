import os
import re
from collections import Counter
from typing import Tuple
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")
urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"
DELETIONS = re.compile(r"(\d+)\Wdeletions")
INSERTIONS = re.compile(r"(\d+)\Winsertions")


def _parse_changes(commit_str) -> int:
    count = 0


def get_min_max_amount_of_commits(
    commit_log: str = commits, year: int = None
) -> Tuple[str, str]:
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    year_count: Counter = Counter()

    with open(commit_log) as f:
        data = f.readlines()

    for line in data:
        date_str, count_str = line.split("|")
        commit_date = parse(date_str[8:])

        if year and commit_date.year != year:
            continue

        m = re.search(INSERTIONS, count_str)
        insertions = int(m.group(1)) if m else 0
        m = re.search(DELETIONS, count_str)
        deletions = int(m.group(1)) if m else 0

        key = YEAR_MONTH.format(y=commit_date.year, m=commit_date.month)
        year_count[key] += deletions + insertions

    most_common = year_count.most_common()
    return most_common[-1][0], most_common[0][0]
