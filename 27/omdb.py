import json
import re


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as f:
            movies.append(json.load(f))
    for movie in movies:
        print(movie["Awards"])
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    return [movie["Title"] for movie in movies if "Comedy" in movie["Genre"]][0]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""

    def _sort_nom(movie):
        res = re.search(r"(\d*) nominations", movie["Awards"])
        return int(res.group(1))

    print(max(movies, key=_sort_nom))
    return max(movies, key=_sort_nom)["Title"]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""

    def _sort_run(movie):
        res = re.search(r"(\d*) min", movie["Runtime"])
        return int(res.group(1))

    print(max(movies, key=_sort_run))
    return max(movies, key=_sort_run)["Title"]
