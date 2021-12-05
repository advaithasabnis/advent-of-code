from collections import defaultdict
from itertools import zip_longest

from .shared import parse_text


def vent_count(coords):
    vent_count = defaultdict(int)
    for (x1, y1), (x2, y2) in coords:
        fill_value = None
        if x1 < x2:
            x_range = range(x1, x2 + 1, 1)
        elif x1 > x2:
            x_range = range(x1, x2 - 1, -1)
        else:
            x_range = []
            fill_value = x1
        if y1 < y2:
            y_range = range(y1, y2 + 1, 1)
        elif y1 > y2:
            y_range = range(y1, y2 - 1, -1)
        else:
            y_range = []
            fill_value = y1
        for i, j in zip_longest(x_range, y_range, fillvalue=fill_value):
            vent_count[(i, j)] += 1
    return vent_count


def main(text):
    coords = parse_text(text)
    vents = vent_count(coords)
    return sum(v > 1 for v in vents.values())


_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()
assert main(_input) == 12
