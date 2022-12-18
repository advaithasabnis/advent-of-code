import re


def crane_operations(text: str, advanced: bool) -> list[list[str]]:
    crates, instructions = (t := text.split('\n\n'))[0].splitlines(), t[1]
    no_of_stacks = len(crates.pop()) // 4 + 1
    stacks: list[list[str]] = [[] for _ in range(no_of_stacks)]

    # Parse initial state of crates
    for row in crates[::-1]:
        for i, crate in enumerate(row[1::4]):
            if crate.isalpha():
                stacks[i].append(crate)

    # Parse instructions
    pattern = re.compile(r'^move (\d+) from (\d+) to (\d+)$', re.M)
    moves = pattern.findall(instructions)

    # Slice crates from the source stack and append them to the destination stack in reverse order
    # This is faster than n pop and append operations
    for n, i, j in moves:
        moved = stacks[int(i) - 1][-int(n) :]
        stacks[int(i) - 1] = stacks[int(i) - 1][: -int(n)]
        if advanced:
            stacks[int(j) - 1].extend(moved)
        else:
            stacks[int(j) - 1].extend(moved[::-1])

    return stacks


def top_crates(stacks: list[list[str]]) -> str:
    return ''.join([s.pop() for s in stacks])
