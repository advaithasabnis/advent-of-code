import operator
from collections import namedtuple

from .shared import eval_infix

opinfo = namedtuple('Operator', ['calc', 'prec'])
operator_info = {
    "+": opinfo(operator.add, 1),
    "*": opinfo(operator.mul, 0),
}


def main(text, operators=operator_info):
    data = text.splitlines()
    result = 0
    for line in data:
        result += eval_infix(line, operators)
    return result
