# Simple solution: 3 loops with improvement
# def main(text: str) -> int:
#     entries = tuple(map(int, text.splitlines()))
#     for i in range(len(entries)):
#         for j in range(i + 1, len(entries)):
#             if entries[i] + entries[j] < 2020:
#                 for k in range(j + 1, len(entries)):
#                     if entries[i] + entries[j] + entries[k] == 2020:
#                         return entries[i] * entries[j] * entries[k]

# Solution using look up in sets assuming there are no duplicate entries
# def main(text: str) -> int:
#     entries = set(map(int, text.splitlines()))
#     for i in entries:
#         for j in entries:
#             if i + j <= 2020:
#                 if (k := 2020 - i - j) in entries:
#                     return i * j * k


# Solution using look up in dict keys. Works if there are duplicates
def main(text: str) -> int:
    from collections import defaultdict
    counter = defaultdict(int)
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


_input = """
1721
979
366
299
675
1456
""".strip()
assert main(_input) == 241861950