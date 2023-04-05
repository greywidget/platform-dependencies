from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6, hour=22, minute=0, second=0)
TIME_UNITS = dict(
    d=lambda x: timedelta(days=x),
    h=lambda x: timedelta(hours=x),
    m=lambda x: timedelta(minutes=x),
    s=lambda x: timedelta(seconds=x),
)


def add_todo(delay_time: str, task: str, start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    target_dt = start_time

    # if no time unit passed = int, return result
    try:
        target_dt += TIME_UNITS["s"](int(delay_time))
    except ValueError:
        matches = re.findall(r"(\d+)([dhms])", delay_time)
        for amount, unit in matches:
            target_dt += TIME_UNITS[unit](int(amount))
    finally:
        return f"{task} @ {target_dt}"
