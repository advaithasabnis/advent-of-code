from .shared import build_graph


def main(text: str) -> int:
    g = build_graph(text)
    return g.accumulator()


_input = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()
assert main(_input) == 5
