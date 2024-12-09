from collections import defaultdict


def main(text: str) -> int:
    grid = defaultdict(str)
    for i, r in enumerate(text.splitlines()):
        for j, c in enumerate(r):
            grid[i, j] = c

    g = [key for key, value in grid.items() if value == 'A']
    D = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    T = ['SMMS', 'MSSM', 'SSMM', 'MMSS']
    count = 0
    for i, j in g:
        sequence = ''.join([grid[i + di, j + dj] for di, dj in D])
        if sequence in T:
            count += 1

    return count


_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()
assert main(_input) == 9
