from .shared import calculate_score


def main(text: str) -> int:
    return calculate_score(text, part=2)


_input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".strip()

assert main(_input) == 1206
