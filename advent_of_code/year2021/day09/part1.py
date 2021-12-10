from .shared import parse_map


def find_risk_levels(height_map):
    risk_levels = []
    directions = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    )
    for (x, y), height in height_map.items():
        for dx, dy in directions:
            if height == 9 or height_map.get((x + dx, y + dy), 9) <= height:
                break
        else:
            risk_levels.append(height + 1)
    return risk_levels


def main(text):
    height_map = parse_map(text)
    risk_levels = find_risk_levels(height_map)
    return sum(risk_levels)


_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()
assert main(_input) == 15
