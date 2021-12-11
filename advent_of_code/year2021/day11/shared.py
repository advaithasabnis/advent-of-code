class DumboGrid:
    def __init__(self, text):
        self.grid = dict()
        for x, line in enumerate(text.splitlines()):
            for y, char in enumerate(line):
                self.grid[(x, y)] = int(char)

        self.size = len(self.grid)
        self.directions = (
            (0, 1),
            (1, 1),
            (-1, 1),
            (1, 0),
            (1, -1),
            (-1, -1),
            (-1, 0),
            (0, -1),
        )
        self.flashed = set()
        self.total_flashes = 0

    def step(self):
        self.flashed = set()
        stack = []
        for coord in self.grid.keys():
            self.grid[coord] += 1
            if self.grid[coord] > 9:
                self.flashed.add(coord)
                stack.append(coord)
                self.grid[coord] = 0
        while stack:
            fx, fy = stack.pop()
            for dx, dy in self.directions:
                neighbour = fx + dx, fy + dy
                if neighbour in self.flashed:
                    continue
                if self.grid.get(neighbour):
                    self.grid[neighbour] += 1
                    if self.grid[neighbour] > 9:
                        self.flashed.add((neighbour))
                        stack.append(neighbour)
                        self.grid[neighbour] = 0
        self.total_flashes += len(self.flashed)
        return self

    def n_steps(self, n):
        for i in range(n):
            self.step()
        return self

    def find_sync_step(self):
        i = 1
        while True:
            self.step()
            if len(self.flashed) == self.size:
                return i
            i += 1
