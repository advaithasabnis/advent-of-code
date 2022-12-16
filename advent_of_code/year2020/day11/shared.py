def parse_map(data):
    s = {}
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == 'L':
                s[(x, y)] = False
    return s


def find_stable_state(s, size, threshold, visibility):
    directions = (
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    )
    ns = s.copy()
    modified = s.keys()
    while True:
        new_modified = set()
        for x, y in modified:
            count = 0
            for dx, dy in directions:
                if visibility:
                    i = 1
                    while True:
                        sx = x + dx * i
                        sy = y + dy * i
                        if sx < 0 or sy < 0 or sx >= size or sy >= size:
                            break
                        if s.get((sx, sy)) == False:
                            break
                        if s.get((sx, sy)):
                            count += 1
                            break
                        i += 1
                    if count >= threshold:
                        break
                else:
                    if s.get((x + dx, y + dy)):
                        count += 1
                        if count >= threshold:
                            break

            if (s.get((x, y))) & (count >= threshold):
                ns[(x, y)] = False
                new_modified.add((x, y))
            elif (not s.get((x, y))) & (count == 0):
                ns[(x, y)] = True
                new_modified.add((x, y))
        if new_modified:
            s = ns.copy()
            modified = new_modified.copy()
        else:
            return s
