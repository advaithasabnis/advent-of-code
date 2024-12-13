from .shared import blink


def main(text: str) -> int:
    return sum(blink(mark, 25) for mark in text.split())


_input = """125 17""".strip()
assert main(_input) == 55312
