from .shared import parse_text


def main(text: str) -> int:
    machines = parse_text(text)
    tokens = 0

    for x1, y1, x2, y2, X, Y in machines:
        X += 10000000000000
        Y += 10000000000000
        det = (x1 * y2) - (x2 * y1)
        # If the determinant is zero, the points are collinear
        if det == 0:
            print("Collinear")  # Input did not contain any collinear points so skipped this case
            continue
        else:
            a = (X * y2 - Y * x2) / det
            b = (x1 * Y - X * y1) / det
            # Prize is achieved only if a and b are positive integers
            if a > 0 and b > 0 and a.is_integer() and b.is_integer():
                tokens += int(3 * a + b)

    return tokens
