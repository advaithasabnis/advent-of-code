from .shared import build_graph


def find_fix(text, reach, leads):
    fixes = {}
    data = text.splitlines()
    for i, row in enumerate(data):
        m = row.split()
        if m[0] == 'acc':
            continue
        else:
            if m[0] == 'nop':
                fixes[i] = i + int(m[1])
            elif m[0] == 'jmp':
                fixes[i] = i + 1
            if i in reach and fixes[i] in leads:
                return i, fixes[i]
    raise AssertionError('Fix not found')


def main(text: str) -> int:
    g = build_graph(text)
    reach, leads = g.BFS(0), g.reverse_BFS(g.size)
    u, v = find_fix(text, reach, leads)
    g.remove_edge(u, g._succ[u])
    g.add_edge(u, v)
    return g.accumulator()


_input = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()
assert main(_input) == 8
