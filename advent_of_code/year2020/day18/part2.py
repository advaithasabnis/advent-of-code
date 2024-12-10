import operator
from collections import namedtuple

from .shared import eval_infix


Operator = namedtuple('Operator', ['calc', 'prec'])
operator_info = {
    "+": Operator(operator.add, 1),
    "*": Operator(operator.mul, 0),
}


def main(text, operators=operator_info):
    data = text.splitlines()
    result = 0
    for line in data:
        result += eval_infix(line, operators)
    return result
