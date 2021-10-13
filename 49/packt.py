from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = "https://bites-data.s3.us-east-2.amazonaws.com/packt.html"
CONTENT = requests.get(PACKT).text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    title = soup.find("div", class_="dotd-title").find("h2").text.strip()

    image = soup.find("img", class_="bookimage imagecache imagecache-dotd_main_image")[
        "src"
    ]

    link = soup.find("div", class_="dotd-main-book-image float-left").find("a")["href"]

    divs = soup.find("div", class_="dotd-main-book-summary float-left").find_all("div")
    description = divs[2].text.strip()

    return Book(title, description, image, link)
