from collections import namedtuple

from bs4 import BeautifulSoup
import requests
import re
from operator import attrgetter

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple("Entry", "title points comments")


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def _get_titles(soup):
    elements = soup.find_all("span", "title")
    text_strings = []
    for element in elements:
        strings = element.find_all("a")
        text1 = strings[0].string
        text2 = f" ({strings[1].string})" if len(strings) > 1 else ""
        text_strings.append(f"{text1}{text2}")

    return text_strings


def _get_counts(soup):
    elements = soup.find_all("span", "controls")
    points = [item.find("span", "smaller").contents[0].strip() for item in elements]
    comments = [item.find_all("a")[1].string for item in elements]

    rg_count = re.compile(r"^\d+")
    comment_counts = [int(rg_count.search(comment).group(0)) for comment in comments]
    point_counts = [int(rg_count.search(point).group(0)) for point in points]

    return [point_counts, comment_counts]


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
    Return a list of top (default = 5) titles ordered descending
    by number of points and comments.
    """
    soup = _create_soup_obj(url)

    titles = _get_titles(soup)
    points, comments = _get_counts(soup)
    data = zip(titles, points, comments)
    entries = [Entry(title, points, comments) for title, points, comments in data]
    # return entries
    return sorted(entries, key=attrgetter("points", "comments"), reverse=True)[:top]
