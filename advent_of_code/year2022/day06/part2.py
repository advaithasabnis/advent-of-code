from .shared import find_marker


def main(text: str) -> int:
    return find_marker(text, 14)


_input = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
""".strip()
assert main(_input) == 19
