from advent_of_code.year2024.day23.shared import Network


def main(text: str) -> str:
    network = Network()
    for edge in text.splitlines():
        u, v = edge.split('-')
        network.add_connection(u, v)

    # Find clique with maximum length
    clique = network.bron_kerbosch_max()

    return ','.join(sorted(clique))


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

assert main(_input) == 'co,de,ka,ta'
