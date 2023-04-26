from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    day = 0
    while True:
        day += num_days
        for _ in range(num_bites):
            yield start_date + timedelta(days=day)
