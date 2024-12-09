# This approach is 6x more performant than one that searches in all directions of X
# (similar to part 2, where we search around As)


Matrix = list[list[str]]


def rotate_45_clockwise(matrix: Matrix) -> Matrix:
    """Rotate the matrix 45 degrees clockwise."""
    rows, cols = len(matrix), len(matrix[0])
    diagonals: Matrix = [[] for _ in range(rows + cols - 1)]

    for i in range(rows):
        for j in range(cols):
            diagonals[i + j].append(matrix[i][j])

    return diagonals


def rotate_45_counterclockwise(matrix: Matrix) -> Matrix:
    """Rotate the matrix 45 degrees counterclockwise."""
    rows, cols = len(matrix), len(matrix[0])
    diagonals: Matrix = [[] for _ in range(rows + cols - 1)]

    for i in range(rows):
        for j in range(cols):
            diagonals[(cols - 1 - j) + i].append(matrix[i][j])

    return diagonals


def transpose(matrix: Matrix) -> Matrix:
    """Transpose a square matrix."""
    return [list(row) for row in zip(*matrix)]


def count_target(matrix, target):
    """Count the number of occurrences of the target string and its reverse in the matrix."""
    count = 0
    for line in matrix:
        larger_str = ''.join(line)
        count += larger_str.count(target) + larger_str.count(target[::-1])
    return count


def main(text: str) -> int:
    """Count the number of occurrences of the target string in the matrix in all orientations."""

    target = 'XMAS'
    matrix = [list(line) for line in text.splitlines()]

    total_count = 0

    transformations = [lambda x: x, transpose, rotate_45_clockwise, rotate_45_counterclockwise]

    for transform in transformations:
        total_count += count_target(transform(matrix), target)

    return total_count


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
assert main(_input) == 18
