from collections import defaultdict


def main(text):
    data = [0] + list(map(int, text.splitlines()))
    data.sort()
    counter = defaultdict(int)
    for i in range(1, len(data)):
        counter[data[i] - data[i - 1]] += 1
    # For the jump from last adapter to device
    counter[3] += 1
    return counter[1] * counter[3]


_input = """
16
10
15
5
1
11
7
19
6
12
4
""".strip()
assert main(_input) == 35
