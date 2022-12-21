from itertools import accumulate

from .shared import parse_input


def main(text: str) -> str:
    reg_change = parse_input(text)

    # Calculate CRT image
    crt = '\n'
    for i, position in enumerate(accumulate(reg_change), 1):
        # If CRT location is within +- 1 of register position, add a '#'
        if (i - 1) % 40 - position in (-1, 0, 1):
            crt += '#'
        else:
            crt += ' '

        # For readability of result, add a newline every 40 characters
        if i % 40 == 0:
            crt += '\n'

    return crt
