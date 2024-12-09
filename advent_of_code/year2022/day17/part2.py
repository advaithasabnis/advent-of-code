from itertools import cycle

from .shared import ROCKS, check


def main(text):
    rocks = cycle(enumerate(ROCKS))
    jets = cycle(enumerate([-1 if x == '<' else 1 for x in text]))

    tower = set()
    tops = [0] * 7
    cache = dict()

    idx, rock = next(rocks)
    jdx, jet = next(jets)

    rounds = int(1e12)

    for step in range(rounds):
        pos = complex(2, max(tops) + 4)  # set start pos
        skyline = tuple(tops[i] - min(tops) for i in range(7))

        key = idx, jdx, skyline
        if key in cache:  # check for cycle
            S, T = cache[key]
            d, m = divmod(rounds - step, step - S)
            if m == 0:
                for i in range(7):
                    tops[i] += (tops[i] - T[i]) * d
                break
        else:
            cache[key] = step, tops.copy()

        while True:
            if check(pos, jet, rock, tower):
                pos += jet  # maybe move side
            if check(pos, -1j, rock, tower):
                pos += -1j  # maybe move down
            else:
                break  # can't move down
            jdx, jet = next(jets)

        tower |= {pos + r for r in rock}  # add rock to tower

        for r in rock:
            point = pos + r
            tops[int(point.real)] = max(tops[int(point.real)], int(point.imag))

        idx, rock = next(rocks)
        jdx, jet = next(jets)

    return int(max(tops))
