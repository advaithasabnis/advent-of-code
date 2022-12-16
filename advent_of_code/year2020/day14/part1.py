from .shared import parse_program


def main(text):
    or_mask = 0
    and_mask = 0
    memory = dict()
    for i in parse_program(text):
        if i[0]:
            memory[i[1]] = (i[2] | or_mask) & and_mask
        else:
            or_mask = int(i[1].replace('X', '0'), 2)
            and_mask = int(i[1].replace('X', '1'), 2)
    return sum(memory.values())


_input = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip()
assert main(_input) == 165
