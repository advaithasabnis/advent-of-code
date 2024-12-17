from collections import Counter

from .shared import parse_input, sign


def main(text: str) -> int:
    robots = parse_input(text)
    cols = 101
    rows = 103
    steps = max(cols, rows)

    min_safety_factor_x, min_safety_factor_y = float("inf"), float("inf")
    best_step_x, best_step_y = 0, 0

    # Iterate over the steps to find the step where safety factor is minimum along x and y axis
    # Low safety factor means that the robots are close to each other
    for step in range(1, steps):
        quadrants: Counter = Counter()
        for x, y, vx, vy in robots:
            fx, fy = (x + vx * step) % cols, (y + vy * step) % rows
            quadrants[(sign(fx, cols // 2), sign(fy, rows // 2))] += 1

        safety_factor_x = (quadrants[(-1, -1)] + quadrants[(-1, 1)]) * (
            quadrants[(1, -1)] + quadrants[(1, 1)]
        )
        safety_factor_y = (quadrants[(-1, -1)] + quadrants[(1, -1)]) * (
            quadrants[(-1, 1)] + quadrants[(1, 1)]
        )

        if safety_factor_x < min_safety_factor_x:
            min_safety_factor_x = safety_factor_x
            best_step_x = step

        if safety_factor_y < min_safety_factor_y:
            min_safety_factor_y = safety_factor_y
            best_step_y = step

    # Chinese Remainder Theorem
    # Find the best step where both x and y axis have minimum safety factor
    # Robots are most likely to be ordered at this step
    best_step = best_step_x + ((pow(cols, -1, rows) * (best_step_y - best_step_x)) % rows) * cols

    # Print the robot positions at the best step and check if a tree is formed
    # Uncomment the following code to print
    # matrix = [["." for _ in range(cols)] for _ in range(rows)]
    # for x, y, vx, vy in robots:
    #     fx, fy = (x + vx * best_step) % cols, (y + vy * best_step) % rows
    #     matrix[fy][fx] = "#"

    # for row in matrix:
    #     print("".join(row))

    return best_step
