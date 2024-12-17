from collections import Counter
from math import prod

from .shared import parse_input, sign


def main(text: str) -> int:
    robots = parse_input(text)
    cols = 101
    rows = 103
    steps = 100

    quadrants: Counter = Counter()
    for x, y, vx, vy in robots:
        fx, fy = (x + vx * steps) % cols, (y + vy * steps) % rows
        quadrants[(sign(fx, cols // 2), sign(fy, rows // 2))] += 1

    safety_factor = prod([quadrants[(i, j)] for i in [1, -1] for j in [1, -1]])

    return safety_factor
