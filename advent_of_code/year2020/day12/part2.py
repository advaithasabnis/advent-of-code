from .shared import rotate


def main(text):
    data = text.splitlines()
    # Ship starting coordinates
    x = y = 0
    # Relative way point coordinates
    wx, wy = 10, 1
    for instruction in data:
        i, n = instruction[0], int(instruction[1:])
        if i == 'F':
            x += wx * n
            y += wy * n
        elif i == 'L':
            wx, wy = rotate(wx, wy, n)
        elif i == 'R':
            wx, wy = rotate(wx, wy, -n)
        elif i == 'N':
            wy += n
        elif i == 'S':
            wy -= n
        elif i == 'E':
            wx += n
        elif i == 'W':
            wx -= n
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
assert main(_input) == 286
