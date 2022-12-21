def parse_input(text: str) -> list[int]:
    instructions = text.splitlines()

    # Store changes to register in each cycle as a list
    reg_change = [1]
    for line in instructions:
        match line.split():
            case ['addx', reg]:
                # Since addx takes two cycles, we need to add 0 to the list first
                reg_change.extend([0, int(reg)])
            case _:
                # No change in register otherwise so append 0
                reg_change.append(0)

    return reg_change
