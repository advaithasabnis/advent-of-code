from itertools import product

from .shared import parse_program


def replacer(input_string, replacing_tuple):
    output_string = input_string.replace('1', '0')
    for i in replacing_tuple:
        output_string = output_string.replace('X', i, 1)
    return output_string


def main(text):
    or_mask = 0
    xor_masks = []
    memory = dict()
    for i in parse_program(text):
        if i[0]:
            address = i[1] | or_mask
            for m in xor_masks:
                memory[address ^ m] = i[2]
        else:
            or_mask = int(i[1].replace('X', '0'), 2)
            xor_masks = []
            for t in product(['0', '1'], repeat=i[1].count('X')):
                xor_masks.append(int(replacer(i[1], t), 2))

    return sum(memory.values())


_input = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip()
assert main(_input) == 208
