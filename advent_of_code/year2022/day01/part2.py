from .shared import parse_calories


def main(text: str) -> int:
    return sum(sorted(parse_calories(text), reverse=True)[0:3])


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
assert main(_input) == 45000
