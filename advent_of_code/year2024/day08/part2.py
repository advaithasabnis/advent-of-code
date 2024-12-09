from collections import defaultdict


def is_within_bounds(pos: tuple[int, int], rows: int, cols: int) -> bool:
    x, y = pos
    return 0 <= x < cols and 0 <= y < rows


def main(text: str) -> int:
    # Parse input grid
    grid: defaultdict[str, list] = defaultdict(list)
    data = text.splitlines()
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if char != '.':
                grid[char].append((i, j))

    rows, cols = len(data), len(data[0])
    antinodes = set()

    for freq, antennas in grid.items():
        for i, a1 in enumerate(antennas):
            for a2 in antennas[i + 1 :]:
                # Add the two antennas themselves
                antinodes.add(a1)
                antinodes.add(a2)

                # Add the resonant antinodes
                x1, y1 = a1
                x2, y2 = a2
                dx, dy = x2 - x1, y2 - y1

                while is_within_bounds((x2 + dx, y2 + dy), rows, cols):
                    antinodes.add((x2 + dx, y2 + dy))
                    x2, y2 = x2 + dx, y2 + dy

                while is_within_bounds((x1 - dx, y1 - dy), rows, cols):
                    antinodes.add((x1 - dx, y1 - dy))
                    x1, y1 = x1 - dx, y1 - dy

    return len(antinodes)


_input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip()

assert main(_input) == 34
