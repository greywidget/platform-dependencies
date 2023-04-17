from datetime import date
from dateutil.rrule import rrule, WEEKLY


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
    is celebrated assuming it's the 2nd Sunday of May."""
    start_date = date(year, 5, 1)

    return rrule(dtstart=start_date, freq=WEEKLY, count=2, byweekday=6)[1].date()


# I quite like the PyBites solution too:

# from dateutil.relativedelta import relativedelta, SU

# MAY = 5

# def get_mothers_day_date(year):
#     """Given the passed in year int, return the date Mother's Day
#        is celebrated assuming it's the 2nd Sunday of May."""
#     first_of_may = date(year=year, month=MAY, day=1)
#     return first_of_may + relativedelta(weeks=1, weekday=SU)
