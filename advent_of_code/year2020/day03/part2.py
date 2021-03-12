from .shared import find_trees


def main(text: str) -> int:
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    product = 1
    for r, d in slopes:
        product *= find_trees(text, r, d)
    return product


_input = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip()
assert main(_input) == 336