from .shared import *


def main(text: str) -> int:
    rows = text.splitlines()
    dim = (len(rows) - 2, len(rows[0]) - 2)

    starting_blizzards = parse_input(rows)

    return find_fastest_time(starting_blizzards, dim, 3)


_input = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
""".strip()
assert main(_input) == 54
