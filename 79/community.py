from collections import Counter
import csv

import requests

CSV_URL = "https://bites-data.s3.us-east-2.amazonaws.com/community.csv"


def get_csv():
    """Use requests to download the csv and return the
    decoded content"""
    resp = requests.get(CSV_URL)
    resp.raise_for_status()
    return resp.text.split("\n")


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
    and their corresponding member counts in pluses to standard output
    """
    reader = csv.DictReader(content)
    counter = Counter([row["tz"] for row in reader])
    for item in sorted(counter):
        print(f"{item:19}| {'+' * counter[item]}")
