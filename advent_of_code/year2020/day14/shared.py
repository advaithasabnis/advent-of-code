import re


def parse_program(text):
    mask = re.compile(r'^mask = ([X\d]+)$')
    mem = re.compile(r'^mem\[(\d+)\] = (\d+)$')
    for line in text.splitlines():
        if m := mem.fullmatch(line):
            yield True, int(m.group(1)), int(m.group(2))
        elif m := mask.fullmatch(line):
            yield False, m.group(1)
