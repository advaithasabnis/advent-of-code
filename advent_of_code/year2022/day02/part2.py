def main(text: str):
    # Assign a number to each outcome or shape
    score_outcome = {
        'X': 0,
        'Y': 1,
        'Z': 2,
    }

    shape_opponent = {
        'A': 0,
        'B': 1,
        'C': 2,
    }
    rounds = text.splitlines()
    score = 0
    for r in rounds:
        opponent, outcome = shape_opponent[(p := r.split())[0]], score_outcome[p[1]]
        # Use modulo for circular logic, e.g. -1 % 3 = 2 (in Python)
        score += ((opponent + outcome - 1) % 3) + 1
        score += outcome * 3
    return score


_input = """
A Y
B X
C Z
""".strip()
assert main(_input) == 12
