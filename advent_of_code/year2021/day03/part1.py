from collections import Counter


def main(text):
    data = text.splitlines()
    gamma = ''
    for i in range(len(data[0])):
        c = Counter()
        for line in data:
            c.update(line[i])
        gamma += c.most_common(1)[0][0]
    gamma = int(gamma, 2)
    epsilon = gamma ^ int('1' * len(data[0]), 2)
    return gamma * epsilon


_input = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()
assert main(_input) == 198
