from datetime import datetime
import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc: datetime, *timezones):
    """Receive a utc datetime and one or more timezones and check if
    they are all within schedule (MEETING_HOURS)"""
    utc = datetime(
        utc.year, utc.month, utc.day, utc.hour, utc.minute, utc.second, tzinfo=pytz.utc
    )
    local_times = []
    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError(f"Timezone {tz} is not valid.")
        local_times.append(utc.astimezone(pytz.timezone(tz)))

    check = [
        item.date() == utc.date() and item.hour in MEETING_HOURS for item in local_times
    ]
    return all(check)
