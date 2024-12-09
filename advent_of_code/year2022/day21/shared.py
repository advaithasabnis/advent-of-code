import operator
from typing import Literal

MathOperator = Literal['+', '-', '*', '/']


def get_operator(operator_str: MathOperator):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    return operators.get(operator_str)


# A binary tree where each node represents a monkey
class Tree:
    def __init__(self, name: str, monkeys: dict[str, list[str]]):
        self.name = name
        self.left = None
        self.right = None
        self.op = None
        self.data = None
        self.monkeys = monkeys

    # Build the tree recursively
    # If a monkey yells a number, set the data to the value
    # If a monkey yells an expression, set the two monkeys on the left and right and the operation
    def build_tree(self):
        m = self.monkeys[self.name]
        if m[0].isnumeric():
            self.data = int(m[0])
        else:
            self.op = m[1]
            self.left = Tree(m[0], self.monkeys)
            self.left.build_tree()
            self.right = Tree(m[2], self.monkeys)
            self.right.build_tree()

    # Calculate the value of the root monkey recursively
    def value(self):
        if self.data:
            return self.data
        else:
            return get_operator(self.op)(self.left.value(), self.right.value())

    # Find the path to a monkey from the root with 'L' and 'R' for left and right branch resp.
    def find_node(self, target_name: str, path=None):
        if path is None:
            path = []

        if self.name == target_name:
            return path

        if self.left is not None:
            left_path = self.left.find_node(target_name, path + ['L'])
            if left_path:
                return left_path

        if self.right is not None:
            right_path = self.right.find_node(target_name, path + ['R'])
            if right_path:
                return right_path

        return None
