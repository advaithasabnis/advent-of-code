import re

COORD_PATTERN = re.compile(r'^(\d+),(\d+) -> (\d+),(\d+)$')


def map_coords(line):
    m = COORD_PATTERN.match(line)
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def parse_text(text):
    return list(map(map_coords, text.splitlines()))
