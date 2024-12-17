import re

from .shared import calculate


def solve(prog: list[int], p: int, A: int) -> int | None:
    """
    Recursive function to solve the program and find the value of A.
    Assumptions:
        - Single loop from start to end until A is 0
        - Output depends on starting value of A, and not B or C
        - Each iteration of the loop prints one numbers
        - Each iteration A is shifted right by 3 bits
        - The loop ends when A reaches 0

    Parameters
    ----------
    prog : list[int]
        The program to solve
    p : int
        The current position in the program
    A : int
        The value of A

    Returns
    -------
    int
        The value of A if found, otherwise None
    """
    # If we reached the start of the program, return the value of A
    if p < 0:
        return A

    output = prog[p]
    # In each iteration of the program, A is shifted right by 3, so in the reverse we shift left by 3
    # For example if in the first iteration A = 3 is valid,
    # in the next iteration A is between 24 and 31 (3 << 3 and 3 << 3 + 7)
    A = A << 3

    # Try all possible values of A until the result matches the current digit
    for i in range(8):
        new_A = A + i
        result = calculate(prog, True, new_A)
        if result and result[0] == output and (final_A := solve(prog, p - 1, new_A)):
            return final_A
    # Return None if no valid A found
    return None


def main(text: str) -> int | None:
    A, B, C, *prog = map(int, re.findall(r'\d+', text))
    # Start from the end of the program
    return solve(prog, len(prog) - 1, 0)


_input = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
""".strip()

assert main(_input) == 117440
