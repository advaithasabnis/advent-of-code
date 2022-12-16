from .shared import find_invalid_num


def main(text: str, p: int = 25) -> int:
    data = tuple(map(int, text.splitlines()))
    index, invalid_num = find_invalid_num(data, p)
    i = 0
    j = 1
    current_sum = data[0]
    while j < len(data):
        while current_sum > invalid_num:
            current_sum -= data[i]
            i += 1
        if current_sum == invalid_num:
            return min(data[i:j]) + max(data[i:j])
        current_sum += data[j]
        j += 1
    return None


_input = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip()
assert main(_input, p=5) == 62
