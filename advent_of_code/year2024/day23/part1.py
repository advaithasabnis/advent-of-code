from advent_of_code.year2024.day23.shared import Network


def main(text: str) -> int:
    network = Network()
    for edge in text.splitlines():
        u, v = edge.split('-')
        network.add_connection(u, v)

    # Find number of cliques that are of size 3
    cliques = network.bron_kerbosch(3)

    # Count the number of cliques that contain at least one node starting with 't'
    count = 0
    for clique in cliques:
        if any(node.startswith('t') for node in clique):
            count += 1

    return count


_input = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip()

main(_input)
