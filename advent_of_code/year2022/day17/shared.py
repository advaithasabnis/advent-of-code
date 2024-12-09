ROCKS = (
    (0, 1, 2, 3),
    (1, 0 + 1j, 2 + 1j, 1 + 2j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 0 + 1j, 0 + 2j, 0 + 3j),
    (0, 1, 0 + 1j, 1 + 1j),
)


def is_empty(pos, tower):
    return pos.real in range(7) and pos.imag > 0 and pos not in tower


def check(pos, dir, rock, tower):
    return all(is_empty(pos + dir + r, tower) for r in rock)
