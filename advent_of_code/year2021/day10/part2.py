from .shared import OPEN_MAP, parse_subsystem


def middle_score(incomplete_lines):
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    auto_score = []
    for line in incomplete_lines:
        score = 0
        for char in line[::-1]:
            score *= 5
            score += scores[OPEN_MAP[char]]
        auto_score.append(score)
    auto_score.sort()
    return auto_score[int((len(auto_score) - 1) / 2)]


def main(text):
    _, incomplete_lines = parse_subsystem(text)
    return middle_score(incomplete_lines)


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
assert main(_input) == 288957
