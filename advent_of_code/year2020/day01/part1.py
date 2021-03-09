# Simple solution: loop inside a loop
# def main(text: str) -> int:
#     entries = tuple(map(int, text.splitlines()))
#     for i in range(len(entries)):
#         for j in range(i + 1, len(entries)):
#             if entries[i] + entries[j] == 2020:
#                 return entries[i] * entries[j]

# Solution using look up in sets assuming there are no duplicate entries
# def main(text: str) -> int:
#     entries = set(map(int, text.splitlines()))
#     for i in entries:
#         if (j := 2020 - i) in entries and i != 1010:
#             return i * j


# Solution using look up in dict keys. Works if there are duplicates
def main(text: str) -> int:
    from collections import defaultdict
    counter = defaultdict(int)
    for x in text.split('\n'):
        counter[int(x)] += 1

    # special case for 1010
    if counter[1010] >= 2:
        return 1010 * 1010

    del counter[1010]

    for i in counter.keys():
        if (j := 2020 - i) in counter.keys():
            return i * j


_input = """
1721
979
366
299
675
1456
""".strip()
assert main(_input) == 514579