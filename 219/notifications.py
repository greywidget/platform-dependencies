from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    delta_days = timedelta(days=num_days)
    bite_date = start_date + delta_days
    bite_count = 0

    while True:
        if bite_count == num_bites:
            bite_count = 0
            bite_date += delta_days
        yield bite_date
        bite_count += 1
