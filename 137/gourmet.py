#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _similarity(wine, cheese):
    wine_count = Counter(wine.lower())
    cheese_count = Counter(cheese.lower())
    common = set(wine_count) & set(cheese_count)

    numerator = sum(
        min(wine_count.get(item), cheese_count.get(item)) for item in common
    )
    denominator = 1 + pow(len(wine) - len(cheese), 2)

    return round(numerator / denominator, 2)


def best_match_per_wine(wine_type="all"):
    """wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    if wine_type == "all":
        wines = [*RED_WINES, *WHITE_WINES, *SPARKLING_WINES]
    elif wine_type == "white":
        wines = WHITE_WINES
    elif wine_type == "red":
        wines = RED_WINES
    elif wine_type == "sparkling":
        wines = SPARKLING_WINES
    else:
        raise ValueError(f"{wine_type} is not valid")

    data = [
        (wine, cheese, _similarity(wine, cheese))
        for wine in wines
        for cheese in CHEESES
    ]
    return max(data, key=operator.itemgetter(2))


def match_wine_5cheeses():
    """pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    wine_5_cheese = []
    wines = [*RED_WINES, *WHITE_WINES, *SPARKLING_WINES]
    for wine in wines:
        data = [(cheese, _similarity(wine, cheese)) for cheese in CHEESES]
        data.sort(key=operator.itemgetter(0))
        data.sort(key=operator.itemgetter(1), reverse=True)
        cheeses = [item[0] for item in data][:5]
        wine_5_cheese.append((wine, cheeses))

    return sorted(wine_5_cheese)
