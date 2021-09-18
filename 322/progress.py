import datetime as dt


def ontrack_reading(books_goal: int, books_read: int, day_of_year: int = None) -> bool:
    current_year = dt.date.today().year
    start = dt.date(current_year, 1, 1)
    end = dt.date(current_year, 12, 31)
    days_in_year = (end - start).days + 1
    current = day_of_year if day_of_year else dt.date.today().timetuple().tm_yday
    return books_read / books_goal >= current / days_in_year
