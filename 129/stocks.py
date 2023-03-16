from collections import defaultdict
import requests

STOCK_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/stocks.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
    - strip off leading '$',
    - if 'M' in cap value, strip it off and return value as float,
    - if 'B', strip it off, multiply by 1,000 and return
      value as float"""
    if cap == "n/a":
        return 0

    cap = cap.replace("$", "")

    if "M" in cap:
        return float(cap.replace("M", ""))

    if "B" in cap:
        return float(cap.replace("B", "")) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
    the _cap_str_to_mln_float to parse the cap values,
    return a float with 2 digit precision"""
    return round(
        sum(
            [
                _cap_str_to_mln_float(item.get("cap"))
                for item in data
                if item.get("industry") == industry
            ]
        ),
        2,
    )


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
    the _cap_str_to_mln_float to parse the cap values"""

    return max(data, key=lambda x: _cap_str_to_mln_float(x.get("cap"))).get("symbol")


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
    discard n/a"""
    sector_stocks = defaultdict(float)

    for item in data:
        if (sector := item.get("sector")) != "n/a":
            sector_stocks[sector] += _cap_str_to_mln_float(item.get("cap"))

    most = max(sector_stocks.items(), key=lambda x: x[1])
    least = min(sector_stocks.items(), key=lambda x: x[1])

    return most[0], least[0]
