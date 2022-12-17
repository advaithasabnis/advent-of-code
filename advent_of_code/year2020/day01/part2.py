from collections import defaultdict


def main(text: str) -> int | float:
    counter: dict[int | float, int] = defaultdict(int)
    for x in text.split('\n'):
        counter[int(x)] += 1

    for i in counter.keys():
        rem = 2020 - i
        if counter[rem / 2] >= 2:
            return i * rem * rem

        del counter[rem / 2]

        for j in counter.keys():
            if i + j <= 2020:
                if (k := rem - j) in counter.keys():
                    return i * j * k
    raise ValueError("No solution found")


_input = """
1721
979
366
299
675
1456
""".strip()
assert main(_input) == 241861950
