from .shared import rotate


def main(text):
    data = text.splitlines()
    # Ship starting coordinates
    x = y = 0
    # Unit vector for direction
    dx, dy = 1, 0
    for instruction in data:
        i, n = instruction[0], int(instruction[1:])
        if i == 'F':
            x += dx * n
            y += dy * n
        elif i == 'L':
            dx, dy = rotate(dx, dy, n)
        elif i == 'R':
            dx, dy = rotate(dx, dy, -n)
        elif i == 'N':
            y += n
        elif i == 'S':
            y -= n
        elif i == 'E':
            x += n
        elif i == 'W':
            x -= n
        else:
            raise ValueError('Invalid instruction')
    return int(abs(x) + abs(y))


_input = """
F10
N3
F7
R90
F11
""".strip()
assert main(_input) == 25
