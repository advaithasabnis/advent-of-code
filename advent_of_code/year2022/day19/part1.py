import multiprocessing

from .shared import parse_input


def get_score_from_bp(bp):
    return bp.id * bp.max_geodes(t=24)


def main(text: str) -> int:
    blueprints = parse_input(text)

    with multiprocessing.Pool() as pool:
        scores = pool.map(get_score_from_bp, blueprints)

    return sum(scores)
