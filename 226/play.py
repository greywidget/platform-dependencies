from collections import namedtuple

from bs4 import BeautifulSoup
from pathlib import Path
from rich import inspect, print
from rich.traceback import install

htmlfile: Path = Path.cwd() / "news.html"

Entry = namedtuple("Entry", "title points comments")


def _create_soup_obj(htmlfile):
    with open(htmlfile, encoding="utf-8") as f:
        html = f.read()

    return BeautifulSoup(html, "html.parser")


def _get_titles(soup):
    table = soup.find_all("table")[1]
    rows = table.find_all("tr")
    print(len(rows))
    return


def main():
    install()
    soup = _create_soup_obj(htmlfile=htmlfile)
    titles = _get_titles(soup)


if __name__ == "__main__":
    main()
