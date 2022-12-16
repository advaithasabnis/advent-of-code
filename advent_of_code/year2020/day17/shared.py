import operator
from collections import defaultdict
from itertools import product


def get_bounds(coords, dimensions=3):
    ranges = []
    for i in range(dimensions):
        ranges.append(
            range(min(coords, key=lambda x: x[i])[i] - 1, max(coords, key=lambda x: x[i])[i] + 2)
        )
    return product(*ranges)


def parse_state(data, dimensions=3):
    s = set()
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == '#':
                s.add((x, y) + (0,) * (dimensions - 2))
    return s


def find_final_state(data, cycles=6, dimensions=3):
    grid = parse_state(data, dimensions)
    directions = [d for d in product([-1, 0, 1], repeat=dimensions)]
    directions.remove((0,) * dimensions)
    for _ in range(cycles):
        new_grid = set()
        inactives = defaultdict(int)
        for coords in grid:
            count = 0
            for delta in directions:
                if (neighbour := tuple(map(operator.add, coords, delta))) in grid:
                    count += 1
                else:
                    inactives[neighbour] += 1
            if count in (2, 3):
                new_grid.add(coords)
        for coords, n_count in inactives.items():
            if n_count == 3:
                new_grid.add(coords)
        grid = new_grid.copy()

    return grid
