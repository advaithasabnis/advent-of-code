import operator
from collections.abc import Callable
from typing import NamedTuple


class Blizzard(NamedTuple):
    i: int  # position in i dimension
    j: int  # position in j dimension
    k1: int  # if it moves in i dimension
    k2: int  # if it moves in j dimension
    op: Callable  # to use for direction of movement


def parse_input(rows: list) -> list[Blizzard]:
    """
    Returns a list of blizzards with their starting positions and directions.
    """
    starting_blizzards = []

    # Skip first and last row since they are walls
    for i, row in enumerate(rows[1:-1]):
        # Skip first and last column since they are walls
        for j, char in enumerate(row[1:-1]):
            if char == '>':
                # Blizzard moving right in the i dimension
                starting_blizzards.append(Blizzard(i, j, 0, 1, operator.add))
            elif char == '<':
                # Blizzard moving left in the i dimension
                starting_blizzards.append(Blizzard(i, j, 0, 1, operator.sub))
            elif char == '^':
                # Blizzard moving up in the j dimension
                starting_blizzards.append(Blizzard(i, j, 1, 0, operator.sub))
            elif char == 'v':
                # Blizzard moving down in the j dimension
                starting_blizzards.append(Blizzard(i, j, 1, 0, operator.add))

    return starting_blizzards


def get_blizzards(starting_blizzards: list, dim: tuple, t: int) -> set:
    """
    Returns the positions of all blizzards at a given time t.

    Positions of blizzards at time t can be calculated by applying the adding or subtracting kt
    to the starting position and then taking the modulo of the dimensions of the map
    to spawn the blizzard on the opposite side of the map if it goes out of bounds.
    """

    blizzards = set()
    for i, j, k1, k2, op in starting_blizzards:
        blizzards.add(((op(i, k1 * t) % dim[0]), (op(j, k2 * t) % dim[1])))
    return blizzards


def is_out_of_bounds(point: tuple, dimensions: tuple) -> bool:
    i, j = point
    a, b = dimensions

    # Check if the point is outside the bounds
    # excluding starting (-1, 0) and end (a, b-1) positions
    if (i < 0 or i >= a) and not (i == -1 and j == 0) and not (i == a and j == b - 1):
        return True
    elif j < 0 or j >= b:
        return True
    else:
        return False


def find_fastest_time(starting_blizzards: list, dim: tuple, N: int) -> int:
    start = (-1, 0)
    goal = (dim[0], dim[1] - 1)
    positions = set()
    positions.add(start)

    directions = (
        (0, 0),
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    )

    trip_count = 1
    for t in range(1, 10_000):
        next_positions = set()
        blizzards = get_blizzards(starting_blizzards, dim, t)

        for s in positions:
            for dx, dy in directions:
                pos = s[0] + dx, s[1] + dy
                if pos not in blizzards and not is_out_of_bounds(pos, dim):
                    next_positions.add(pos)

        if goal in next_positions:
            if trip_count == N:
                return t
            next_positions = {goal}
            start, goal = goal, start
            trip_count += 1

        positions = next_positions

    raise Exception("No solution found")
