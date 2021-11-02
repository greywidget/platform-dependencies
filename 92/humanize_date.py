from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple("TimeOffset", "offset date_str divider")

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, "just now", None),
    TimeOffset(MINUTE, "{} seconds ago", None),
    TimeOffset(2 * MINUTE, "a minute ago", None),
    TimeOffset(HOUR, "{} minutes ago", MINUTE),
    TimeOffset(2 * HOUR, "an hour ago", None),
    TimeOffset(DAY, "{} hours ago", HOUR),
    TimeOffset(2 * DAY, "yesterday", None),
)
DATEFMT = "%m/%d/%y"


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
    using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError("Please pass a datetime <= current time")

    total_seconds = (NOW - date).total_seconds()

    for time_offset in TIME_OFFSETS:
        if total_seconds < time_offset.offset:
            delta = int(total_seconds)
            if time_offset.divider:
                delta //= time_offset.divider
            return time_offset.date_str.format(delta)

    return date.strftime(DATEFMT)
