import re
from collections import defaultdict
from operator import and_, or_, xor
from typing import Callable


OPERATOR_MAP = {"AND": and_, "OR": or_, "XOR": xor}
type Operator = Callable[[int, int], int]


class DiGraph:
    """
    A directed graph representation of the circuit.

    ready_wires[wire] = The value of the wire.
    gates[output_wire] = (op, input1, input2)
    gate_to_output[(op, input1, input2)] = output_wire
    input_to_gate[input_wire] = {gate1, gate2, ...}
    """

    def __init__(self):
        self.ready_wires = dict()
        self.gates = dict()
        self.gate_to_output = dict()
        self.input_to_gate = defaultdict(set)

    def add_gate(self, op: Operator, inp1: str, inp2: str, out_wire: str):
        # Store inputs as a sorted tuple, so (x00, y00) is the same as (y00, x00)
        sorted_inp = tuple(sorted([inp1, inp2]))
        self.gates[out_wire] = (op, sorted_inp[0], sorted_inp[1])
        self.gate_to_output[(op, sorted_inp[0], sorted_inp[1])] = out_wire
        # Add input to gate mapping for quick gate lookup when inputs are ready
        self.input_to_gate[inp1].add(out_wire)
        self.input_to_gate[inp2].add(out_wire)


def build_graph(text: str) -> DiGraph:
    g = DiGraph()
    # Split input into block of initial values and logic gates data
    init_values, data = text.split("\n\n")
    # Parse initial values
    for row in init_values.splitlines():
        u, w = row.split(": ")
        g.ready_wires[u] = int(w)
    # Parse logic gates
    pattern = re.compile(r"(.+) (AND|OR|XOR) (.+) -> (.+)")
    for row in data.splitlines():
        if m := pattern.match(row):
            inp1, op, inp2, out = m.groups()
            g.add_gate(OPERATOR_MAP[op], inp1, inp2, out)
        else:
            raise ValueError(f"Invalid gate definition: {row}")

    return g
