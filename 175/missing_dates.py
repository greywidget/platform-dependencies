from datetime import date, timedelta


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
    of missing datetime.date objects (no worries about order).

    You can assume that the first and last date of the
    range is always present (assumption made in tests).

    See the Bite description and tests for example outputs.
    """

    dates.sort()
    date_from = dates[0]
    a_day = timedelta(days=1)
    missing_dates = []
    a_date = date_from

    for item in dates:
        while item != a_date:
            missing_dates.append(a_date)
            a_date += a_day
        a_date += a_day
    return missing_dates
