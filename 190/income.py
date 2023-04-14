import os
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from urllib.request import urlretrieve

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / "countries.xml"

if not countries.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/countries.xml", countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    data = defaultdict(list)
    ns = {"ctry": "http://www.worldbank.org"}
    root = ET.parse(countries).getroot()

    for country in root.findall("ctry:country", ns):
        data[country.find("ctry:incomeLevel", ns).text].append(
            country.find("ctry:name", ns).text
        )
    return data
