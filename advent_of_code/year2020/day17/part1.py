from .shared import find_final_state


def main(text):
    data = text.splitlines()
    final_state = find_final_state(data, 6, 3)
    return len(final_state)


_input = """
.#.
..#
###
""".strip()
assert main(_input) == 112
