from .shared import build_regex, parse_text


def main(text):
    rules, messages = parse_text(text)
    pattern = build_regex(rules)
    count = 0
    for msg in messages:
        if pattern.fullmatch(msg):
            count += 1
    return count


_input = """
0: 1 2
1: 3
2: 3 + 4 +
3: "a"
4: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".strip()
