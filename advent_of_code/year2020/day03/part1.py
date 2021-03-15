from .shared import find_trees


def main(text: str) -> int:
    return find_trees(text, 3, 1)


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
assert main(_input) == 7
