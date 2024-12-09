from collections import Counter


def main(text: str) -> int:
    pairs = [map(int, line.split()) for line in text.splitlines()]
    left, right = zip(*pairs)
    occurences = Counter(right)
    similarity = sum(n * occurences[n] for n in left)
    return similarity


_input = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()
main(_input)
assert main(_input) == 31
