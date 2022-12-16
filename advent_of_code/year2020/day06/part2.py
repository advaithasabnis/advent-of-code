import string


def main(text: str) -> int:
    data = text.split('\n\n')
    count = 0
    for person in data:
        s = set(string.ascii_lowercase)
        for row in person.split('\n'):
            s = set.intersection(s, set(row))
            if len(s) == 0:
                break
        count += len(s)
    return count


_input = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip()

assert main(_input) == 6
