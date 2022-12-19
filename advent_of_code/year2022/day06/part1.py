from .shared import find_marker


def main(text: str) -> int:
    return find_marker(text, 4)


_input = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
""".strip()
assert main(_input) == 7
