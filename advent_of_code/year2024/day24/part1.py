from collections import deque

from advent_of_code.year2024.day24.shared import build_graph


def main(text: str) -> int:
    g = build_graph(text)

    # Gates that have both inputs ready
    ready_gates: deque[str] = deque()
    for out_wire, (op, inp1, inp2) in g.gates.items():
        if inp1 in g.ready_wires and inp2 in g.ready_wires:
            ready_gates.append(out_wire)

    # Evaluate gates in topological order
    while ready_gates:
        # Pop the next gate to evaluate
        out = ready_gates.popleft()
        op, inp1, inp2 = g.gates[out]
        # Evaluate the gate and set the output wire as ready
        g.ready_wires[out] = op(g.ready_wires[inp1], g.ready_wires[inp2])

        # Check if any gates that depend on this output are now ready
        for nxt in g.input_to_gate[out]:
            _, nxt_inp1, nxt_inp2 = g.gates[nxt]
            # If all inputs are ready, add the gate to the ready queue
            if nxt_inp1 in g.ready_wires and nxt_inp2 in g.ready_wires:
                ready_gates.append(nxt)

    # Get the output wire values and concatenate them to get the final output
    z_wires = [w for w in sorted(g.ready_wires, reverse=True) if w.startswith("z")]
    output = "".join(str(g.ready_wires[w]) for w in z_wires)

    return int(output, 2)


_input = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
""".strip()

assert main(_input) == 2024
