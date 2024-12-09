# Idea from https://www.reddit.com/r/adventofcode/comments/1h8l3z5/comment/m0tv6di/

from math import log10


def digits(n: int) -> int:
    """Return the number of digits in n"""
    return int(log10(n)) + 1


def endswith(a: int, b: int) -> bool:
    """Return True if a ends with b"""
    return (a - b) % 10 ** digits(b) == 0


def is_tractable(test_value: int, numbers: list[int], check_concat=True) -> bool:
    """
    Determine if the given numbers can be combined using addition, multiplication,
    or concatenation (if enabled) to produce the target value.

    This function uses a recursive approach with pruning to explore only valid
    paths, significantly reducing computational overhead.

    Parameters
    ----------
    test_value : int
        The target value we aim to produce.
    numbers : list of int
        A list of numbers to combine using the allowed operators.
    check_concat : bool, optional
        Whether to consider concatenation as a valid operation (default is True).

    Returns
    -------
    bool
        True if the numbers can produce the `test_value` using the operators,
        False otherwise.
    """
    *head, n = numbers

    # Base case: If only one number remains, check if it matches the target value
    if not head:
        return n == test_value

    # Case 1: Multiplication - Check divisibility and recurse
    q, r = divmod(test_value, n)
    if r == 0 and is_tractable(q, head, check_concat):
        return True

    # Case 2: Concatenation - Check if `test_value` ends with `n` and recurse
    if (
        check_concat
        and endswith(test_value, n)
        and is_tractable(test_value // (10 ** digits(n)), head, check_concat)
    ):
        return True

    # Case 3: Addition - Subtract `n` and recurse
    if is_tractable(test_value - n, head, check_concat):
        return True

    # If no case succeeds, return False
    return False
