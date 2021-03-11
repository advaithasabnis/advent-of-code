import re


def main(text: str) -> int:
    pattern = re.compile(r'^(\d+)-(\d+) (\w): (.*)$', re.M)
    count = 0
    for i, j, letter, text in pattern.findall(text):
        if (text[int(i) - 1] == letter) != (text[int(j) - 1] == letter):
            count += 1
    return count


_input = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip()
assert main(_input) == 1