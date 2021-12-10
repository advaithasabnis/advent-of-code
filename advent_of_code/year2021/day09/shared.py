def parse_map(text):
    height_map = {}
    for x, line in enumerate(text.splitlines()):
        for y, char in enumerate(line):
            height_map[(x, y)] = int(char)
    return height_map
