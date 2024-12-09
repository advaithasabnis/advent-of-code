from .shared import Tree


def main(text: str):
    monkeys = dict()

    for row in text.splitlines():
        name, expression = row.split(':')
        monkeys[name] = expression.split()

    monkey_tree = Tree('root', monkeys)
    monkey_tree.build_tree()

    # Find the path to the 'humn' node which we want to find the value for
    path = monkey_tree.find_node('humn')

    # Along the path to the target node (x), calculate the value of the right hand side
    # For example if x + v = RHS, then x = RHS - v
    # or if x * v = RHS, then x = RHS / v
    # or if v / x = RHS, then x = v / RHS and so on
    branch = monkey_tree
    rhs = None
    for direction in path:
        op = branch.op
        if direction == 'L' and branch.right is not None:
            v = branch.right.value()
            if rhs is None:
                rhs = v
            elif op == '/':
                rhs = rhs * v
            elif op == '*':
                rhs = rhs / v
            elif op == '+':
                rhs = rhs - v
            elif op == '-':
                rhs = rhs + v
            branch = branch.left
        if direction == 'R' and branch.left is not None:
            v = branch.left.value()
            if rhs is None:
                rhs = v
            elif op == '/':
                rhs = v / rhs
            elif op == '*':
                rhs = rhs / v
            elif op == '+':
                rhs = rhs - v
            elif op == '-':
                rhs = v - rhs
            branch = branch.right

    assert rhs is not None
    return int(rhs)


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
assert main(_input) == 301
