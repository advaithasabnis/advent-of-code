from collections import deque


Pos = tuple[int, int]


def shortest_path(blockers: set[Pos], dimensions: int) -> int:
    """
    Find the shortest path from (0, 0) to (dimensions - 1, dimensions - 1) in a grid
    of size dimensions x dimensions, where blockers are obstacles.

    Parameters
    ----------
    blockers : set[Pos]
        Set of blocked positions.
    dimensions : int
        Dimensions of the grid.

    Returns
    -------
    int
        Shortest path length. -1 if no path is found.

    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start, goal = (0, 0), (dimensions - 1, dimensions - 1)

    queue: deque[tuple[Pos, int]] = deque([(start, 0)])
    visited = set([start])

    while queue:
        (x, y), dist = queue.popleft()

        if (x, y) == goal:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < dimensions
                and 0 <= ny < dimensions
                and (nx, ny) not in visited
                and (nx, ny) not in blockers
            ):
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

    return -1
