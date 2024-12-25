from collections import defaultdict
from itertools import combinations


class Network:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_connection(self, u: str, v: str):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bron_kerbosch(self, k=None):
        """
        Bron-Kerbosch algorithm for finding all maximal cliques in a graph or
        all cliques (non-maximal) of a certain size.

        If k is None, all maximal cliques are returned. Otherwise, all cliques
        of size k are returned.
        """

        def bk(r, p, x):
            # If the current clique is of the desired size, yield it
            if k and len(r) == k:
                yield r
                return None
            elif not k and not p and not x:
                yield r
            # Continue the search
            for v in list(p):
                yield from bk(r | {v}, p & set(self.graph[v]), x & set(self.graph[v]))
                p.remove(v)
                x.add(v)

        r, p, x = set(), set(self.graph.keys()), set()
        yield from bk(r, p, x)

    def bron_kerbosch_max(self):
        """Bron-Kerbosch algorithm for finding the maximum clique in a graph"""
        max_clique = set()

        def bk(r, p, x):
            nonlocal max_clique
            # If the max possible clique is less than the current maximum clique, return
            if len(r) + len(p) <= len(max_clique):
                return None
            # If at the end, and clique is larger than the current maximum, update the maximum
            if not p and not x:
                if len(r) > len(max_clique):
                    max_clique = r.copy()
                return None
            # Otherwise, continue the search
            for v in list(p):
                bk(r | {v}, p & set(self.graph[v]), x & set(self.graph[v]))
                p.remove(v)
                x.add(v)

        r, p, x = set(), set(self.graph.keys()), set()
        bk(r, p, x)
        return max_clique
