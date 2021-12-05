from collections import Counter


def oxy(data):
    valid = data.copy()
    for i in range(len(data[0])):
        new = []
        c = Counter()
        for line in valid:
            c.update(line[i])
        if c['0'] > c['1']:
            gamma = '0'
        else:
            gamma = '1'
        for line in valid:
            if line[i] == gamma:
                new.append(line)
        valid = new.copy()
        if len(valid) == 1:
            break
    return valid[0]


def co2(data):
    valid = data.copy()
    for i in range(len(data[0])):
        new = []
        c = Counter()
        for line in valid:
            c.update(line[i])
        if c['0'] <= c['1']:
            gamma = '0'
        else:
            gamma = '1'
        for line in valid:
            if line[i] == gamma:
                new.append(line)
        valid = new.copy()
        if len(valid) == 1:
            break
    return valid[0]


def main(text):
    data = text.splitlines()
    oxygen_rating = oxy(data)
    co2_rating = co2(data)
    return int(oxygen_rating, 2) * int(co2_rating, 2)


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
assert main(_input) == 230
