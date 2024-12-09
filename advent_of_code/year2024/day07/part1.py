from .shared import is_tractable


def main(text: str) -> int:
    ans1 = 0
    for line in text.splitlines():
        test_value, *numbers = map(int, line.replace(':', '').split())
        if is_tractable(test_value, numbers, check_concat=False):
            ans1 += test_value
    return ans1


_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()

assert main(_input) == 3749
