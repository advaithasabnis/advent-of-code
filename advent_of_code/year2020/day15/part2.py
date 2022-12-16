from .shared import find_last_spoken


def main(text):
    starting_numbers = [int(m) for m in text.split(',')]
    return find_last_spoken(starting_numbers, 30_000_000)


_input = "0,3,6"
assert main(_input) == 175594
