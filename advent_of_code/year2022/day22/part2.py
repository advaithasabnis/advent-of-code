from .shared import Net, parse_input, password


def main(text: str) -> int:
    bounds, walls, steps = parse_input(text)
    net = Net(bounds)

    pos = net.start_pos
    direction = net.start_direction

    # Execute each step in the instructions
    for turn, n in steps:
        direction *= turn
        for _ in range(n):
            # Move one place along the net with wrapping
            next_pos, next_direction = net.move(pos, direction)

            # If the resulting position is a wall, stop
            if next_pos in walls:
                break
            pos, direction = next_pos, next_direction

    return password(pos, direction)


_input = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".strip(
    '\n'
)
assert main(_input) == 5031
