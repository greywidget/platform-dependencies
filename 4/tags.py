import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed", tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# def get_pybites_top_tags(n=10):
#     """use Counter to get the top 10 PyBites tags from the feed
#     data already loaded into the content variable"""
#     cats = []
#     root = ET.fromstring(content)
#     for child in root:
#         for item in child:
#             for category in item.findall("category"):
#                 cats.append(category.text)

#     counter = Counter(cats)
#     return counter.most_common(n)


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
    data already loaded into the content variable"""
    tree = ET.fromstring(content)
    tags = (e.text for e in tree.findall("./channel/item/category"))
    return Counter(tags).most_common(n)
