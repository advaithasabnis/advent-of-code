from .shared import count_cheats, find_path


def main(text: str, min_time_saved: int = 100) -> int:
    path = find_path(text)

    # Now count cheats with Manhattan distance in [2, 20].
    return count_cheats(path, min_time_saved, min_dist=2, max_dist=2)


_input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip()

assert main(_input, 1) == 44
assert main(_input, 20) == 5
