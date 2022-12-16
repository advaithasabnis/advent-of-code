from collections import defaultdict, deque


class DiGraph:
    def __init__(self):
        # the predecessors of node n are stored in the ddict self._pred
        # the successors of node n are stored in the dict self._succ
        # the accumulator change is stored in the dict self._acc
        self._pred = defaultdict(set)
        self._succ = {}
        self._acc = {}
        self.size = 0

    def add_node(self, u, w):
        self._acc[u] = w

    def add_edge(self, u, v, w=None):
        # add the edge
        self._succ[u] = v
        self._pred[v].add(u)
        self.size = len(self._succ)
        # Update w if provided
        if w is not None:
            self.add_node(u, w)

    def remove_edge(self, u, v):
        self._succ.pop(u)
        self._pred[v].remove(u)

    def BFS(self, u):
        visited = set()
        queue = deque()
        queue.append(u)
        while queue:
            node = queue.pop()
            if node not in visited:
                visited.add(node)
                queue.append(self._succ[node])
        return visited

    def reverse_BFS(self, v):
        visited = set()
        queue = deque()
        queue.append(v)
        while queue:
            node = queue.pop()
            if node not in visited:
                visited.add(node)
                queue.extend(self._pred[node])
        return visited

    def accumulator(self):
        visited = set()
        i = 0
        count = 0
        while i < self.size and i not in visited:
            visited.add(i)
            count += self._acc[i]
            i = self._succ[i]
        return count


def build_graph(text):
    g = DiGraph()
    data = text.splitlines()
    for u, row in enumerate(data):
        m = row.split()
        if m[0] == 'nop':
            g.add_edge(u, u + 1, 0)
        elif m[0] == 'acc':
            g.add_edge(u, u + 1, int(m[1]))
        elif m[0] == 'jmp':
            g.add_edge(u, u + int(m[1]), 0)
        else:
            raise ValueError('Unknown instruction type')
    return g
