from .shared import build_regex, parse_text


def main(text):
    rules, messages = parse_text(text)
    rules['11'] = [['42', '+', '31', '+']]
    pattern = build_regex(rules)
    regex_42 = build_regex(rules, '42')
    regex_31 = build_regex(rules, '31')
    count = 0
    for msg in messages:
        if pattern.fullmatch(msg):
            idx = 0
            count_42 = 0
            while True:
                m = regex_42.match(msg, idx)
                if m is None:
                    break
                idx = m.end()
                count_42 += 1

            count_31 = 0
            while True:
                m = regex_31.match(msg, idx)
                if m is None:
                    break
                idx = m.end()
                count_31 += 1
            if count_31 < count_42:
                count += 1
    return count


_input = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 + 31 +
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".strip()
