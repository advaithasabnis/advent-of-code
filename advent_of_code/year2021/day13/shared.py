import re


class TransparentPaper:
    def __init__(self, text):
        data, instructions = text.split('\n\n')

        # Read instructions
        ins_pattern = re.compile(r'^fold along ([xy])=(\d+)$', re.M)
        self.instructions = ins_pattern.findall(instructions)

        # Read dot positions on paper
        self.grid = set()
        for line in data.splitlines():
            self.grid.add(tuple(map(int, line.split(','))))

    def fold_along_x(self, position):
        new_grid = set()
        for x, y in self.grid:
            if x > position:
                new_grid.add((2 * position - x, y))
            elif x < position:
                new_grid.add((x, y))
        self.grid = new_grid

    def fold_along_y(self, position):
        new_grid = set()
        for x, y in self.grid:
            if y > position:
                new_grid.add((x, 2 * position - y))
            elif y < position:
                new_grid.add((x, y))
        self.grid = new_grid

    def execute_instructions(self, n=None):
        for axis, position in self.instructions[:n]:
            if axis == 'x':
                self.fold_along_x(int(position))
            else:
                self.fold_along_y(int(position))
