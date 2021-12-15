from .shared import most_minus_least


def main(text):
    return most_minus_least(text, 40)


_input = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip()
assert main(_input) == 2188189693529
