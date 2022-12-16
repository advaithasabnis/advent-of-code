def get_combinations(n):
    """
    For a number, n of jolage adapters separated by 1 jolt differences,
    this function returns the number of possible combinations.
    """
    return 1 + n * (n + 1) // 2 if n > 0 else 1


def main(text: str) -> int:
    data = [0] + list(map(int, text.splitlines()))
    data.sort()
    group_len = 0
    product = 1
    for i in range(1, len(data)):
        delta = data[i] - data[i - 1]
        if delta == 1:
            group_len += 1
        if delta == 3:
            product *= get_combinations(group_len - 1)
            group_len = 0
    product *= get_combinations(group_len - 1)
    return product


_input = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip()
assert main(_input) == 19208
