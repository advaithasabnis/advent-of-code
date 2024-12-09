from .shared import Tree


class Monkey:
    def __init__(self, n=None):
        self.number = n
        self.op = None
        self.left = None
        self.right = None


# Solve without using a solver / exec
# This method is more than 100x faster than exec
def main(text: str):
    monkeys = dict()

    for row in text.splitlines():
        name, expression = row.split(':')
        monkeys[name] = expression.split()

    monkey_tree = Tree('root', monkeys)
    monkey_tree.build_tree()

    return int(monkey_tree.value())


_input = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".strip()
assert main(_input) == 152
