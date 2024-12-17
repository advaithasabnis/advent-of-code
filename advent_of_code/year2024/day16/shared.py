import heapq
from collections import defaultdict


def parse_input(text: str) -> tuple[set[complex], complex, complex]:
    data = text.splitlines()
    # Set of cells that can be visited
    spaces: set[complex] = set()

    # Find the set of cells that can be visited, the start and the end
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell != '#':
                spaces.add(complex(i, j))
            if cell == 'S':
                start = complex(i, j)
            if cell == 'E':
                end = complex(i, j)

    return spaces, start, end


def find_optimal_path(spaces: set[complex], start: complex, end: complex) -> tuple[int, int]:
    """Find the path from the start to the end in the maze with minimum score."""

    # queue of (score, tiebreaker, position, direction, path)
    # Tiebreaker is used to break ties in the priority queue
    t = 0
    queue = [(0, t, start, 1j, [start])]

    # Dictionary to store the minimum score to reach a position with a direction
    score_upto: defaultdict[tuple[complex, complex], float] = defaultdict(lambda: float('inf'))

    # Minimum total score to reach the end
    min_score = float('inf')

    # Set of cells in any of the best paths
    best_path_cells = set()

    # Rotations to change the direction. 1: moving forward, -1j: turning left, 1j: turning right
    rotations = [1, -1j, 1j]

    # While there are still cells to explore
    while queue:
        # Pop the tuple with the lowest score to explore that path further
        score, _, pos, prev_dir, path = heapq.heappop(queue)

        # If the current position and direction can be reached with a lower score, skip
        # Without this check, the algorithm takes a long time to run
        if score > score_upto[(pos, prev_dir)]:
            continue

        score_upto[(pos, prev_dir)] = score

        # If the current position is the end and the score is less than the minimum score,
        # update the minimum score and the set of cells in the best path
        if pos == end and score <= min_score:
            min_score = score
            best_path_cells.update(path)
            continue

        # For each move, calculate the new position
        for rot in rotations:
            new_pos = pos + prev_dir * rot
            # If the new position can be visited, calculate the new score and add it to the queue
            if new_pos in spaces:
                # If moving in the same direction, the score increases by 1
                # Otherwise, the score increases by 1001 (1000 for turning and 1 for moving)
                new_score = score + 1 if rot == 1 else score + 1001
                t += 1
                heapq.heappush(queue, (new_score, t, new_pos, prev_dir * rot, path + [new_pos]))

    return int(min_score), len(best_path_cells)
