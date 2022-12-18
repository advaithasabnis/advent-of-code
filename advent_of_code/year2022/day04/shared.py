def parse_assignments(text: str) -> list[tuple[range, range]]:
    assignments = text.splitlines()
    sections = []
    for pair in assignments:
        elf1_range, elf2_range = [x.split('-') for x in pair.split(",")]
        elf1 = range(*map(int, elf1_range))
        elf2 = range(*map(int, elf2_range))
        sections.append((elf1, elf2))
    return sections
