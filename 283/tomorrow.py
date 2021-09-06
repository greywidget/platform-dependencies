import datetime


def tomorrow(from_date=datetime.date.today()):
    return from_date + datetime.timedelta(days=1)


if __name__ == "__main__":
    print(tomorrow(datetime.date(2020, 7, 9)))
