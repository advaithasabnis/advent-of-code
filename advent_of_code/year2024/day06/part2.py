from collections import defaultdict


def is_within_bounds(pos: complex, rows: int, cols: int) -> bool:
    """Check if a position is within the grid bounds."""
    return 0 <= pos.real < cols and 0 <= pos.imag < rows


def main(text: str) -> int:
    blocks = set()

    # Step 1: Parse the input grid as complex numbers to represent positions
    grid = text.splitlines()
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            if char == '^':
                start = complex(i, j)
            elif char == '#':
                blocks.add(complex(i, j))

    rows, cols = len(grid), len(grid[0])

    # Step 2: Create a jump table for the entire grid
    jump_table = defaultdict(tuple)

    for pos in {complex(x, y) for x in range(cols) for y in range(rows)}:
        if pos not in blocks:
            for d in [1, -1, 1j, -1j]:
                next_pos = pos + d
                # Continue in the same direction until a block or out of bounds
                while (
                    0 <= next_pos.real < cols
                    and 0 <= next_pos.imag < rows
                    and next_pos not in blocks
                ):
                    next_pos += d
                # If the position is a block, step back and turn right and jump there
                if next_pos in blocks:
                    jump_table[(pos, d)] = (next_pos - d, d * 1j)
                # If posution is out of bounds, jump there
                else:
                    jump_table[(pos, d)] = (next_pos, d)

    # Step 3: Calculate new obstacle positions
    obstacle_positions = set()  # Valid obstacle positions
    checked_obstacles = set()  # Checked obstacle positions

    # Simulate guard's movement
    current_pos = start
    current_dir = -1j

    while is_within_bounds(current_pos, rows, cols):
        # Check for new obstacles in segments of the guard's original path
        start_pos, start_dir = current_pos, current_dir
        end_pos, end_dir = jump_table[(current_pos, current_dir)]

        # Check new obstacle positions between start_pos and end_pos
        obstacle_pos = start_pos + start_dir
        while obstacle_pos != end_pos + start_dir and is_within_bounds(obstacle_pos, rows, cols):
            # If the obstacle position has already been checked, move to the next position
            if obstacle_pos in checked_obstacles:
                obstacle_pos += start_dir
                continue

            # Mark the obstacle position as checked
            checked_obstacles.add(obstacle_pos)

            # Simulate the guard's movement from one step behind the new obstacle
            # As path before the obstacle is deterministic
            pos = obstacle_pos - start_dir
            direction = start_dir
            seen = set()

            while is_within_bounds(pos, rows, cols) and obstacle_pos != start:
                # If the guard has already visited the same position and direction, the path is cyclic
                if (pos, direction) in seen:
                    obstacle_positions.add(obstacle_pos)
                    break

                seen.add((pos, direction))

                if pos.real != obstacle_pos.real and pos.imag != obstacle_pos.imag:
                    pos, direction = jump_table[(pos, direction)]
                else:
                    next_pos = pos + direction
                    if next_pos in blocks or next_pos == obstacle_pos:
                        direction *= 1j
                    else:
                        pos = next_pos

            # Move to the next obstacle position in the direction
            obstacle_pos += start_dir

        # Move to the next segment of the guard's original path
        current_pos, current_dir = end_pos, end_dir

    return len(obstacle_positions)


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

assert main(_input) == 6
