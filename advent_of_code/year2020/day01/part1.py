from collections import defaultdict


def main(text: str) -> int:
    counter: dict[int, int] = defaultdict(int)
    for x in text.split('\n'):
        counter[int(x)] += 1

    # special case for 1010
    if counter[1010] >= 2:
        return 1010 * 1010

    del counter[1010]

    for i in counter.keys():
        if (j := 2020 - i) in counter.keys():
            return i * j

    raise ValueError("No solution found")


_input = """
1721
979
366
299
675
1456
""".strip()
assert main(_input) == 514579
