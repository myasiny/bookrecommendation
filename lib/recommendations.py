from math import sqrt
from typing import List, Dict, Callable


def _sim_pearson(
        prefs: Dict,
        p1: str,
        p2: str
) -> float:
    """
    This method calculates similarity score between two items by the Pearson formula.
    :param prefs: Dataset in json format.
    :param p1: Item to find its similar.
    :param p2: Item to find its similarity to the given one.
    :return: Similarity score.
    """

    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)
    if n == 0:
        return 0

    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    sum1_sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2_sq = sum([pow(prefs[p2][it], 2) for it in si])
    p_sum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n))

    if den == 0:
        return 0

    return num / den


def top_matches(
        prefs: Dict,
        person: str,
        n: int = 3,
        similarity: Callable = _sim_pearson
) -> List[List[str]]:
    """
    This method takes the entire data and calculates the most similar items to the given one.
    :param prefs: Dataset in json format.
    :param person: Item to find its similar.
    :param n: Number of similar items to find.
    :param similarity: Function to calculate distances.
    :return: List of similar items and their similarity scores.
    """

    scores = [(round(similarity(prefs, person, other), 2), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()

    return scores[0:n]
