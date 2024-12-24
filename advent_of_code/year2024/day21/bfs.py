"""
This code is not used in the final solution, but it is a useful snippet to keep around.
It builds a list of possible shortest paths between keys on a numeric or a directional keypad
including zig-zag paths using BFS. The paths in the actual solution are only L-shaped
to minimize changing directions and to keep the lenths of the final paths as short as possible.
"""

from collections import deque


# Adjacency Graphs for Numeric Keypad and Directional Keypad
def build_adjacency_numpad():
    """
    Return a dict mapping key -> list of (neighbor, direction) pairs.
    Keypad layout:
        7 (0,0)   8 (0,1)   9 (0,2)
        4 (1,0)   5 (1,1)   6 (1,2)
        1 (2,0)   2 (2,1)   3 (2,2)
                  0 (3,1)   A (3,2)

    Each entry: adjacency[key] = [(neighborKey, arrowNeeded), ...]
    """
    return {
        '7': [('8', '>'), ('4', 'v')],
        '8': [('7', '<'), ('9', '>'), ('5', 'v')],
        '9': [('8', '<'), ('6', 'v')],
        '4': [('7', '^'), ('5', '>'), ('1', 'v')],
        '5': [('4', '<'), ('6', '>'), ('2', 'v'), ('8', '^')],
        '6': [('5', '<'), ('9', '^'), ('3', 'v')],
        '1': [('4', '^'), ('2', '>')],
        '2': [('1', '<'), ('3', '>'), ('5', '^'), ('0', 'v')],
        '3': [('2', '<'), ('6', '^'), ('A', 'v')],
        '0': [('2', '^'), ('A', '>')],
        'A': [('3', '^'), ('0', '<')],
    }


def build_adjacency_dirpad():
    """
    Return a dict mapping key -> list of (neighbor, direction) pairs.
    Keypad layout:
                 ^ (0,1)  A (0,2)
        < (1,0)  v (1,1)  > (1,2)

    Each entry: adjacency[key] = [(neighborKey, arrowNeeded), ...]
    """
    return {
        '^': [('A', '>'), ('v', 'v')],
        'A': [('^', '<'), ('>', 'v')],
        '<': [('v', '>')],
        'v': [('<', '<'), ('^', '^'), ('>', '>')],
        '>': [('A', '^'), ('v', '<')],
    }


# BFS to Find All Shortest Arrow-Paths from one key to another
def find_all_shortest_direction_sequences(start, end, adjacency):
    """
    Use BFS to find all shortest arrow-sequences from 'start' key to 'end' key.
    Returns a list of direction-strings, e.g. ['<<', 'v<'] if those are equally short.

    adjacency: e.g. adjacency[startKey] = [(neighborKey, arrowChar), ...]

    If start == end, we return [[]] by definition (no moves needed).

    Parameters
    ----------
    start : str
        The starting key.
    end : str
        The ending key.
    adjacency : dict[str, list[tuple[str, str]]]
        The adjacency graph for the keypad.

    Returns
    -------
    list[str]
        A list of direction-strings that are the shortest paths from start to end.
    """
    if start == end:
        return [[]]  # trivial: no moves

    queue = deque()
    queue.append((start, ''))  # (current_key, direction_sequence)

    visited_dist = {start: 0}
    shortest_distance = None
    results = []

    while queue:
        current_key, current_dir_seq = queue.popleft()
        current_dist = len(current_dir_seq)

        if shortest_distance is not None and current_dist > shortest_distance:
            # We've already found shorter paths to 'end'
            continue

        if current_key == end:
            # BFS ensures current_dist is the shortest
            if shortest_distance is None:
                shortest_distance = current_dist
            # Save the direction path
            results.append(current_dir_seq)
            # Don't expand further from 'end'
            continue

        # Expand neighbors
        for neighbor, direction in adjacency[current_key]:
            new_dist = current_dist + 1
            # If neighbor not visited, or found same-dist path:
            if (neighbor not in visited_dist) or (visited_dist[neighbor] == new_dist):
                visited_dist[neighbor] = new_dist
                queue.append((neighbor, current_dir_seq + direction))

    return results
