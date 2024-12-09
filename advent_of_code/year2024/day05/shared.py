from collections import defaultdict, deque


class Graph:
    def __init__(self, rules: str) -> None:
        """
        Initialize the graph from a set of rules.
        """
        self.graph: defaultdict[int, list[int]] = defaultdict(list)
        self.parse_rules(rules)

    def parse_rules(self, rules: str) -> None:
        """
        Parse the rules and build the adjacency list.
        """
        for rule in rules.splitlines():
            x, y = map(int, rule.split('|'))
            self.graph[x].append(y)

    def is_valid(self, lst: list[int]) -> bool:
        """
        Check if a given list adheres to the rules defined by the graph.
        """
        position = {num: idx for idx, num in enumerate(lst)}

        for x in self.graph:
            for y in self.graph[x]:
                # Ensure x appears before y in the list
                if position.get(x, 0) > position.get(y, float('inf')):
                    return False

        return True

    def topological_sort(self, subset: set[int]) -> list[int]:
        """
        Perform a topological sort on a subset of nodes.
        """
        in_degree: defaultdict[int, int] = defaultdict(int)
        for node in subset:
            for neighbor in self.graph[node]:
                if neighbor in subset:
                    in_degree[neighbor] += 1

        queue = deque([node for node in subset if in_degree[node] == 0])
        sorted_order = []

        while queue:
            node = queue.popleft()
            sorted_order.append(node)
            for neighbor in self.graph[node]:
                if neighbor in subset:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

        if len(sorted_order) != len(subset):
            raise ValueError("Unexpected cycle in the subset (should not happen).")

        return sorted_order
