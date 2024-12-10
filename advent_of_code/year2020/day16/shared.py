import re
from typing import NamedTuple


RULES = re.compile(r'(^[\w\s]+?): (\d+)-(\d+) or (\d+)-(\d+)$', re.M)


class Rule(NamedTuple):
    field: str
    l1: int
    u1: int
    l2: int
    u2: int


def parse_notes(text):
    data = text.split('\n\n')
    rules = [
        Rule(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        for m in RULES.finditer(data[0])
    ]
    my_ticket = tuple(map(int, data[1].splitlines()[1].split(',')))
    nearby_tickets = []
    for t in data[2].splitlines()[1:]:
        nearby_tickets.append(tuple(map(int, t.split(','))))
    return rules, my_ticket, nearby_tickets


def optimize_rules(rules):
    r = []
    for _, l1, u1, l2, u2 in rules:
        r.append((l1, u1))
        r.append((l2, u2))
    r = sorted(r, key=lambda x: x[0])
    opt_rules = []
    start = r[0][0]
    end = r[0][1]
    for s, e in r[1:]:
        if s > end + 1:
            opt_rules.append((start, end))
            start = s
            end = e
        else:
            if e > end:
                end = e
    opt_rules.append((start, end))
    return opt_rules
