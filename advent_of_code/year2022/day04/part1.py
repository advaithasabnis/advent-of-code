from .shared import parse_assignments


def main(text: str) -> int:
    sections = parse_assignments(text)
    count = 0
    # Count pairs where a range is fully contained in another
    for elf1, elf2 in sections:
        if (elf1.start >= elf2.start and elf1.stop <= elf2.stop) or (
            elf2.start >= elf1.start and elf2.stop <= elf1.stop
        ):
            count += 1
    return count


_input = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()
assert main(_input) == 2
