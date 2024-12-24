"""
Multi-layer keypad expansion program.

This code:
1) Build a list of possible shortest paths between keys on a numeric keypad
   or a directional keypad. The paths are L-shaped to minimize direction changes.
2) For a given input code like '029A', it splits that into pairs of
   transitions on the numeric keypad, finds all minimal arrow-sequences
   for each pair, then expands those sequences across multiple
   directional keypad layers using recursion and caching.
3) The main function calculates the "complexity" of a list of input codes

Thanks to https://www.reddit.com/r/adventofcode/comments/1hjx0x4/2024_day_21_quick_tutorial_to_solve_part_2_in/
for a tutorial on how to solve this problem efficiently.
"""

import re
from collections import defaultdict
from functools import cache


# Find two possible L shaped paths between two buttons on the keypads
def find_all_shortest_direction_sequences(
    start: str, end: str, coords: dict[str, tuple[int, int]]
) -> set[str]:
    """
    List of all shortest paths between start and end on a numeric or directional keypad.

    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+

    Each path is a list of characters ['^', 'v', '<', '>'] representing the direction of the move.
    The path cannot go over a blank space (e.g. 0 -> 1 is not '<^' but '^<').
    Path is an L shape to minimize changing directions. e.g 6 -> 7 is '<<^' instead of '<^<'
    All shortest paths including zig-zag paths can also be found by BFS but are not needed here.

        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """

    if start == end:
        return {''}

    sx, sy = coords[start]
    ex, ey = coords[end]
    dx, dy = ex - sx, ey - sy

    # Two possible paths: horizontal then vertical, or vertical then horizontal
    paths = set()
    # If we can go horizontally first (the corner cell is not empty)
    if (ex, sy) in coords.values():
        path1 = '>' * dx + '<' * -dx + 'v' * dy + '^' * -dy
        paths.add(path1)
    # If we can go vertically first (the corner cell is not empty)
    if (sx, ey) in coords.values():
        path2 = 'v' * dy + '^' * -dy + '>' * dx + '<' * -dx
        paths.add(path2)

    return paths


# Build a dictionary of all shortest arrow-sequences between all key pairs
def find_shortest_paths(pad_type: str) -> dict[str, dict[str, set[str]]]:
    """
    For pad_type in {'numpad','dirpad'}, build a dict:
       paths[startKey][endKey] = list of all shortest arrow-sequences
    """
    if pad_type == 'numpad':
        # adj = build_adjacency_numpad()
        coords = {
            '7': (0, 0),
            '8': (1, 0),
            '9': (2, 0),
            '4': (0, 1),
            '5': (1, 1),
            '6': (2, 1),
            '1': (0, 2),
            '2': (1, 2),
            '3': (2, 2),
            '0': (1, 3),
            'A': (2, 3),
        }
        keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
    elif pad_type == 'dirpad':
        # adj = build_adjacency_dirpad()
        coords = {
            '^': (1, 0),
            'A': (2, 0),
            '<': (0, 1),
            'v': (1, 1),
            '>': (2, 1),
        }
        keys = ['^', '<', 'v', '>', 'A']
    else:
        raise ValueError(f"Invalid pad_type: {pad_type}")

    paths: defaultdict[str, dict[str, set[str]]] = defaultdict(dict)

    for i in keys:
        for j in keys:
            if i == j:
                paths[i][j] = {''}
            else:
                # Find all shortest arrow-sequences from i to j
                sequences = find_all_shortest_direction_sequences(i, j, coords)
                paths[i][j] = sequences

    return paths


# Expand directional paths for a single layer
dir_paths = find_shortest_paths('dirpad')


def build_seq(
    keys: str,
    index: int = 0,
    prev_key: str = 'A',
    curr_path: str = '',
    result: list[str] | None = None,
) -> list[str]:
    """
    Given a string of "keys" (like '<A', or 'v<<A', etc.), recursively
    build all expansions (arrow sequences + 'A' presses) that move from
    'prev_key' to keys[index], then press 'A', etc.
    """
    if result is None:
        result = []

    # If we've reached the end of the keys, add the current path to the result
    if index == len(keys):
        result.append(curr_path)
        return result

    # For each path from prev_key to keys[index], recurse
    for path in dir_paths[prev_key][keys[index]]:
        build_seq(keys, index + 1, keys[index], curr_path + path + 'A', result)

    return result


# Expand directional paths across multiple layers and calculate the shortest path length
# Cache the results of shortest_seq to avoid recalculating the same paths
@cache
def shortest_seq(keys: str, depth: int) -> int:
    """
    Expand 'keys' across 'depth' layers of directional keypads.

    - If depth == 0, we return the length of 'keys' so far.
    - If depth > 0, we split 'keys' with regex r'.*?A' to get subkeys
      that end in 'A'. For each subkey, we build all expansions at
      the top layer (build_seq(...)), then recursively call shortest_seq
      on each expansion with depth - 1. We take the min over them
      (since we want the shortest expansions overall).

    Returns an integer representing minimal *length* of the final expansion,
    not the expansions themselves.
    """
    if depth == 0:
        return len(keys)

    score = 0
    subkey_list = re.findall(r'.*?A', keys)
    for subkey in subkey_list:
        seq_list = build_seq(subkey)
        m = min(shortest_seq(seq, depth - 1) for seq in seq_list)
        score += m

    return score
