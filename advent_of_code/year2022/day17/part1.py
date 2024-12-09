from itertools import cycle

from .shared import ROCKS, check


def main(text):
    rocks = cycle(ROCKS)
    jets = cycle([-1 if x == '<' else 1 for x in text])

    tower = set()
    tops = [0] * 7

    rock = next(rocks)
    jet = next(jets)

    for _ in range(2022):
        pos = complex(2, max(tops) + 4)  # set start pos

        while True:
            if check(pos, jet, rock, tower):
                pos += jet  # maybe move side
            if check(pos, -1j, rock, tower):
                pos += -1j  # maybe move down
            else:
                break  # can't move down
            jet = next(jets)

        tower |= {pos + r for r in rock}  # add rock to tower

        for r in rock:
            point = pos + r
            tops[int(point.real)] = max(tops[int(point.real)], int(point.imag))

        rock = next(rocks)
        jet = next(jets)

    return int(max(tops))
