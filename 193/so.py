import requests
from bs4 import BeautifulSoup
from operator import itemgetter

cached_so_url = "https://bites-data.s3.us-east-2.amazonaws.com/so_python.html"


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
    parse the questions out of the html with BeautifulSoup,
    filter them by >= 1m views ("..m views").
    Return a list of (question, num_votes) tuples ordered
    by num_votes descending (see tests for expected output).
    """
    data = requests.get(url=url).text
    soup = BeautifulSoup(data, "html.parser")
    posts = soup.find_all("div", "question-summary")
    post_summary = []
    for post in posts:
        views = post.find("div", "views").string
        if "m views" in views:
            question = post.find("a", "question-hyperlink").string.strip()
            votes = int(post.find("span", "vote-count-post").string.strip())
            post_summary.append((question, votes))

    return sorted(post_summary, key=itemgetter(1), reverse=True)
