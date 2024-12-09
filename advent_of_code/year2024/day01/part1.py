def main(text: str) -> int:
    pairs = [map(int, line.split()) for line in text.splitlines()]
    left, right = map(list, zip(*pairs))
    left, right = sorted(left), sorted(right)
    distance = sum(abs(l - r) for l, r in zip(left, right))
    return distance


_input = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()
main(_input)
assert main(_input) == 11
