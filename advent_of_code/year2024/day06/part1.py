def main(text: str) -> int:
    # Parse the input grid as complex numbers to represent positions
    blocks = set()
    grid = text.splitlines()
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            if char == '^':
                start = complex(i, j)
            elif char == '#':
                blocks.add(complex(i, j))

    rows, cols = len(grid), len(grid[0])

    # Simulate guard's movement
    visited = set()
    pos = start
    direction = -1j
    while 0 <= pos.real < cols and 0 <= pos.imag < rows:
        visited.add(pos)
        # next position is a block, turn right
        if pos + direction in blocks:
            direction *= 1j

        pos += direction

    return len(visited)


_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()

assert main(_input) == 41
