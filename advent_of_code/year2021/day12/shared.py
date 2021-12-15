from collections import defaultdict


class CaveSystem:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_connection(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, u, d, visited, path, part2, dup=None):
        pos_paths = []

        # Mark the node 'u' as visited if islower and add to path
        if u.islower():
            visited.add(u)
        path.append(u)

        # If current node is same as end, then append the total path
        if u == d:
            pos_paths.append(path.copy())
        else:
            # If current node is not destination
            # For all the nodes adjacent to this vertex
            for i in self.graph[u]:
                # If node is not yet in visited, recursively find paths
                if i not in visited:
                    pos_paths += self.DFS(i, d, visited, path, part2, dup)
                # If part2 then one lower case node can be visited once again
                elif part2:
                    if dup is None and i.islower() and i != 'start':
                        pos_paths += self.DFS(i, d, visited, path, False, i)

        # Remove current node from path[] and visited
        path.pop()
        visited.discard(u)
        # Put back the node that was visited twice
        visited.add(dup)

        return pos_paths

    def find_all_paths(self, s='start', d='end', part2=False):
        visited = set()
        path = []
        return self.DFS(s, d, visited, path, part2)


def cave_system(text):
    caves = CaveSystem()
    for line in text.splitlines():
        u, v = line.split('-')
        caves.add_connection(u, v)
    return caves
