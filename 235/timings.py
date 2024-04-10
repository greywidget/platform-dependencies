import os
from dataclasses import dataclass
from decimal import Decimal
from operator import itemgetter
from pathlib import Path
from urllib.request import urlretrieve

from rich import print

tmp = Path(os.getenv("TMP", "/tmp"))
timings_log = tmp / "pytest_timings.out"
if not timings_log.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out", timings_log
    )


@dataclass
class Bite:
    bite: str
    nbr_tests: str
    total_time: str
    avg_time: Decimal = None


get_bite_details = itemgetter(0, 2, -3)


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    fastest_bite: Bite = None
    for line in timings:
        if "passed" in line:
            chunks = line.strip().split(" ")
            bite = Bite(*get_bite_details(chunks))
            avg_time = Decimal(bite.total_time) / Decimal(bite.nbr_tests)
            if not fastest_bite or avg_time < fastest_bite.avg_time:
                fastest_bite = bite
                fastest_bite.avg_time = avg_time
    return fastest_bite.bite


if __name__ == "__main__":
    lines = [line for line in timings_log.read_text().strip().split("\n")]
    print(get_bite_with_fastest_avg_test(lines))
