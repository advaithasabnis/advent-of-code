from .shared import is_valid


def main(text: str) -> int:
    reports = [list(map(int, line.split())) for line in text.splitlines()]
    safe = sum((is_valid(report, True) or is_valid(report[::-1], True)) for report in reports)

    return safe


_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()
assert main(_input) == 4
