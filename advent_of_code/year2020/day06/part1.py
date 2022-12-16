def main(text: str) -> int:
    data = text.split('\n\n')
    count = 0
    for person in data:
        count += len(set([char for char in person if char.isalpha()]))
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

assert main(_input) == 11
