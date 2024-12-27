from operator import and_, or_, xor
from typing import Callable

from advent_of_code.year2024.day24.shared import DiGraph, build_graph


type Operator = Callable[[int, int], int]
type Gate = tuple[Operator, str, str]


def swap_outputs(
    gate_to_output: dict[Gate, str], gates: dict[str, Gate], out1: str, out2: str
) -> None:
    gate1 = gates[out1]
    gate2 = gates[out2]

    gate_to_output[gate1] = out2
    gate_to_output[gate2] = out1
    gates[out1] = gate2
    gates[out2] = gate1


def get_gate_output(gate_to_output: dict[Gate, str], op: Operator, inp1: str, inp2: str) -> str:
    sorted_inputs = tuple(sorted({inp1, inp2}))
    return gate_to_output[(op, sorted_inputs[0], sorted_inputs[1])]


def check_ripple_carry_adder(g: DiGraph, bit_length=45):
    # For each bit position i:
    #   sum_i = (x_i XOR y_i) XOR carry_in
    #   carry_out = (x_i AND y_i) OR (carry_in AND (x_i XOR y_i))
    # Compare with actual outputs and track mismatches. Fix swaps to continue.

    mistakes: set[str] = set()
    carry_in: str = ''

    for i in range(0, bit_length):
        if len(mistakes) >= 8:
            break

        try:
            # By puzzle definition, only output wires have possibly been swapped
            # We will always find an s_1, we just need to check if s_1 is correct
            s_1 = g.gate_to_output[(xor, f'x{i:02d}', f'y{i:02d}')]

            # If i == 0, we don't have a carry_in
            if i != 0:
                s_2 = get_gate_output(g.gate_to_output, xor, s_1, carry_in)
            else:
                s_2 = s_1
            # Check if the output wire is correct, sum_i should be z{i:02d}
            if s_2 != f'z{i:02d}':
                mistakes.update([s_2, f'z{i:02d}'])
                # Fix the mistake
                swap_outputs(g.gate_to_output, g.gates, s_2, f'z{i:02d}')

        except KeyError as e:
            # It means s_2 wasn't found, so either s_1 or carry_in is wrong
            # The inputs to get z{i:02d} should be inp1, inp2
            # The symmetric difference of the inputs should be the swapped inputs
            op, inp1, inp2 = g.gates[f'z{i:02d}']

            swap_1, swap_2 = set([inp1, inp2]) ^ {s_1, carry_in}
            mistakes.update([swap_1, swap_2])
            # Fix the mistake
            swap_outputs(g.gate_to_output, g.gates, swap_1, swap_2)
            # Recalculate s_1 and s_2
            s_1 = g.gate_to_output[(xor, f'x{i:02d}', f'y{i:02d}')]
            # s_2 = get_gate_output(g.gate_to_output, op, inp1, inp2) => no need to recalculate

        # First part of the carry out will always be able to be calculated
        carry_i1 = g.gate_to_output[(and_, f'x{i:02d}', f'y{i:02d}')]
        try:
            if i != 0:
                carry_i2 = get_gate_output(g.gate_to_output, and_, carry_in, s_1)
                carry_out = get_gate_output(g.gate_to_output, or_, carry_i1, carry_i2)
            else:
                carry_out = carry_i1

            carry_in = carry_out
        except KeyError as e:
            # No such error found so it hasn't been addressed in this code
            print(f'Mismatch at carry bit {i}:', e)
            break

    return sorted(mistakes)


def main(text: str, bit_length: int = 45) -> str:
    g = build_graph(text)
    mistakes = check_ripple_carry_adder(g, bit_length)
    return ','.join(mistakes)
