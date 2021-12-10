from collections import Counter

from .shared import parse_subsystem


def error_score(illegal_chars):
    c = Counter(illegal_chars)
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
    return sum(count * scores[char] for char, count in c.items())


def main(text):
    illegal_chars, _ = parse_subsystem(text)
    return error_score(illegal_chars)


_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".strip()
assert main(_input) == 26397
