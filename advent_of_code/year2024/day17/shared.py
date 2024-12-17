def calculate(prog: list[int], break_early: bool, A: int, B: int = 0, C: int = 0) -> list[int]:
    """
    Perform program calculations based on the given program and initial values of A, B, and C.\
    
    Parameters
    ----------
    prog : list
        The program to execute.
    break_early : bool
        Whether to break early for part 2.
    A : int
        The initial value of A.
    B : int
        The initial value of B.
    C : int
        The initial value of C.

    Returns
    -------
    list
        The result of the calculations.
    """

    result = []
    idx = 0
    # Loop through the program
    # For my input, the program can be condensed to the following:
    # B = (A & 7 ^ 5 ^ 6) ^ (A >> (A & 7 ^ 5))
    while idx < len(prog):
        combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}
        op = prog[idx + 1]
        match prog[idx]:
            case 0:
                A = A >> combo[op]
            case 1:
                B = B ^ op
            case 2:
                B = combo[op] & 7
            case 3:
                idx = op - 2 if A else idx
            case 4:
                B = B ^ C
            case 5:
                result.append(combo[op] & 7)
                # For part 2 we can break early
                if break_early:
                    break
            case 6:
                B = A >> combo[op]
            case 7:
                C = A >> combo[op]
        idx += 2
    return result
