from .shared import crane_operations, top_crates


def main(text: str) -> str:
    stacks = crane_operations(text, False)
    return top_crates(stacks)


_input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".strip(
    '\n'
)
assert main(_input) == 'CMZ'
