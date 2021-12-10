OPEN_CHARS = tuple('({[<')
CLOSE_CHARS = tuple(')}]>')
OPEN_MAP = dict(zip(OPEN_CHARS, CLOSE_CHARS))
CLOSE_MAP = dict(zip(CLOSE_CHARS, OPEN_CHARS))


def parse_subsystem(text):
    corrupt_chars = []
    incomplete_lines = []
    for line in text.splitlines():
        queue = []
        for i in line:
            if i in OPEN_CHARS:
                queue.append(i)
            elif i in CLOSE_CHARS:
                if not queue or CLOSE_MAP[i] != queue.pop():
                    # Line is corrupt
                    corrupt_chars.append(i)
                    break
        else:
            if queue:
                # Line is incomlete
                incomplete_lines.append(queue)
            else:
                # Line is complete
                pass
    return corrupt_chars, incomplete_lines
