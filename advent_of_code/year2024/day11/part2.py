from .shared import blink


def main(text: str) -> int:
    return sum(blink(mark, 75) for mark in text.split())
