import re

from .shared import calculate


def main(text: str) -> str:
    A, B, C, *prog = map(int, re.findall(r'\d+', text))
    result = calculate(prog, False, A, B, C)
    return ','.join(map(str, result))


_input = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()

assert main(_input) == '4,6,3,5,6,3,5,2,1,0'
