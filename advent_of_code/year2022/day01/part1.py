from .shared import parse_calories


def main(text: str) -> int:
    return max(parse_calories(text))


_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip()
assert main(_input) == 24000
