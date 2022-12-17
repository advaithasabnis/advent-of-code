def main(text: str):
    # Assign a number to each shape
    shape_you = {
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
        opponent, you = shape_opponent[(p := r.split())[0]], shape_you[p[1]]
        # Use modulo for circular logic, e.g. -1 % 3 = 2 (in Python)
        score += ((you - opponent + 1) % 3) * 3
        score += you + 1
    return score


_input = """
A Y
B X
C Z
""".strip()
assert main(_input) == 15
