from datetime import date, timedelta


def tomorrow(from_date=None):
    if from_date is None:
        from_date = date.today()
    return from_date + timedelta(days=1)


if __name__ == "__main__":
    print(tomorrow(date(2020, 7, 9)))
