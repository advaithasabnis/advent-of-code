import math
from collections import defaultdict, deque

from .shared import parse_map


class Graph:
    def __init__(self):
        self._pred = defaultdict(list)

    def add_link(self, u, v):
        self._pred[u].append(v)

    def BFS(self, u):
        visited = set()
        queue = deque()
        queue.append(u)
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for i in self._pred[node]:
                    queue.append(i)
        return visited


def find_basins(height_map):
    minima = []
    height_graph = Graph()
    directions = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    )
    for (x, y), height in height_map.items():
        is_minima = True
        for dx, dy in directions:
            if height_map.get((x + dx, y + dy), 9) <= height:
                if height != 9:
                    height_graph.add_link((x + dx, y + dy), (x, y))
                is_minima = False
        else:
            if is_minima:
                minima.append((x, y))
    basins = []
    for m in minima:
        basins.append(len(height_graph.BFS(m)))
    return basins


def main(text):
    height_map = parse_map(text)
    basins = find_basins(height_map)
    return math.prod(sorted(basins, reverse=True)[:3])


_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()
assert main(_input) == 1134
