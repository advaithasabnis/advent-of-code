from collections import defaultdict

from .shared import parse_text


def vent_count(coords):
    vent_count = defaultdict(int)
    for (x1, y1), (x2, y2) in coords:
        if x1 == x2:
            y1, y2 = sorted((y1, y2))
            for i in range(y1, y2 + 1):
                vent_count[(x1, i)] += 1
        elif y1 == y2:
            x1, x2 = sorted((x1, x2))
            for i in range(x1, x2 + 1):
                vent_count[(i, y1)] += 1
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
assert main(_input) == 5
