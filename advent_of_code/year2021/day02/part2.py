def main(text: str) -> int:
    data = text.splitlines()
    vertical_pos = 0
    horizontal_pos = 0
    aim = 0
    for line in data:
        direction, distance = (c := line.split())[0], int(c[1])
        if direction == 'forward':
            horizontal_pos += distance
            vertical_pos += aim * distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
    return vertical_pos * horizontal_pos


_input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()
assert main(_input) == 900
