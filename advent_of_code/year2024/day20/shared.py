Pos = tuple[int, int]


def build_offsets(min_dist: int, max_dist: int) -> list[Pos]:
    """
    Returns all (dr, dc) pairs for which the Manhattan distance
    min_dist <= |dr| + |dc| <= max_dist.
    """
    offsets = []
    for dr in range(-max_dist, max_dist + 1):
        for dc in range(-max_dist, max_dist + 1):
            manhattan = abs(dr) + abs(dc)
            if min_dist <= manhattan <= max_dist:
                offsets.append((dr, dc))
    return offsets


def count_cheats(path: list[Pos], min_time_saved: int, min_dist: int, max_dist: int) -> int:
    """
    Counts the number of 'cheats' in a path that saves at least min_time_saved.
    Counts by checking all possible offsets in the given Manhattan distance range
    for each cell in the path.

    Parameters
    ----------
    path : list[tuple[int, int]]
        The path to check for cheats
    min_time_saved : int
        The minimum time saved to count a cheat
    min_dist : int
        The minimum Manhattan distance to check
    max_dist : int
        The maximum Manhattan distance to check

    Returns
    -------
    int
        The number of cheats found in the path

    """
    # Build offsets once
    offsets = build_offsets(min_dist, max_dist)

    # Create a lookup for cell positions in the path
    cell_to_index = {cell: i for i, cell in enumerate(path)}

    cheats = 0
    for i, (r, c) in enumerate(path[:-min_time_saved]):
        # Check all offsets within range
        # This is faster than checking all cells in the path ahead (O(L^2))
        # Time complexity is O(L * offsets) where L is the path length
        for dr, dc in offsets:
            nr, nc = r + dr, c + dc
            j = cell_to_index.get((nr, nc))
            # Check if j is valid and if the position is reached 'too soon'
            if j is not None and j >= i + min_time_saved + abs(dr) + abs(dc):
                cheats += 1
    return cheats


def find_path(text: str) -> list[Pos]:
    """
    Parses the maze from the given text, finds S (start) and E (end),
    and returns a list of cells representing the path from S to E.
    """
    maze = text.splitlines()
    rows, cols = len(maze), len(maze[0])

    # Identify start and end points
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    # Raise error if start or end is not found
    if start is None or end is None:
        raise ValueError("Start or end not found in maze")

    visited = set()
    path = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    r, c = start

    # Reconstruct the path by moving step by step
    while (r, c) != end:
        visited.add((r, c))
        path.append((r, c))
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if maze[nr][nc] != '#' and (nr, nc) not in visited:
                r, c = nr, nc
                break

    path.append(end)
    return path
