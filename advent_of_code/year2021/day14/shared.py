from collections import Counter
from functools import cache


def parse_manual(text):
    template, rules = text.split('\n\n')
    rules = dict(r.split(' -> ') for r in rules.splitlines())
    return template, rules


def most_minus_least(text, steps):
    template, rules = parse_manual(text)

    @cache
    def insert(a, b, depth):
        if depth == 0:
            return Counter()
        else:
            e = rules[a + b]
            return Counter(e) + insert(a, e, depth - 1) + insert(e, b, depth - 1)

    elements = Counter(template)
    for i in range(len(template) - 1):
        elements += insert(template[i], template[i + 1], steps)

    return max(elements.values()) - min(elements.values())
