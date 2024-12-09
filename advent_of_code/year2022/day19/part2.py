import multiprocessing
from math import prod

from .shared import parse_input


def get_score_from_bp(bp):
    return bp.max_geodes(t=32)


def main(text: str) -> int:
    blueprints = parse_input(text)

    with multiprocessing.Pool() as pool:
        scores = pool.map(get_score_from_bp, blueprints[:3])

    return prod(scores)
