from .shared import parse_text


def main(text: str) -> int:
    machines = parse_text(text)
    tokens = 0

    for x1, y1, x2, y2, X, Y in machines:
        # Solve the system of equations:
        # a*x1 + b*x2 = X
        # a*y1 + b*y2 = Y
        # where a and b are the number of pushes for buttons A and B, respectively
        det = (x1 * y2) - (y1 * x2)
        # If the determinant is zero, the points are collinear
        if det == 0:
            print("Collinear")  # Input did not contain any collinear points so skipped this case
            continue
        else:
            a = (X * y2 - Y * x2) / det
            b = (x1 * Y - X * y1) / det
            # Prize is achieved only if a and b are positive integers
            if a >= 0 and b >= 0 and a.is_integer() and b.is_integer():
                tokens += int(3 * a + b)

    return tokens


_input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip()

assert main(_input) == 480
