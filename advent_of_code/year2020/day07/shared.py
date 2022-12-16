import re
from collections import defaultdict, deque


class DiGraph:
    def __init__(self):
        # the predecessors of node n are stored in the ddict self._pred
        # the successors of node n are stored in the dict self._succ
        self._pred = defaultdict(dict)  # predecessor
        self._succ = defaultdict(dict)  # successor

    def add_edge(self, u, v, w):
        # add the edge
        self._succ[u][v] = w
        self._pred[v][u] = w

    def DFS(self, u):
        count = 1
        for v, w in self._succ[u].items():
            count += w * self.DFS(v)
        return count

    def reverse_BFS(self, v):
        visited = set()
        queue = deque()
        queue.append(v)
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for i in self._pred[node]:
                    queue.append(i)
        return visited


def build_graph(text):
    g = DiGraph()
    parent_pattern = re.compile(r"^(.+) bags contain (.+)\.$")
    children_pattern = re.compile(r"(\d+) (.+?) bags?")
    data = text.splitlines()
    for row in data:
        m = parent_pattern.match(row)
        parent = m.group(1)
        for amount, child in children_pattern.findall(m.group(2)):
            g.add_edge(parent, child, int(amount))
    return g
