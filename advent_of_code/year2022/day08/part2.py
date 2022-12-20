rot90 = lambda A: [*map(list, zip(*A[::-1]))]


def main(text: str) -> int:
    # Read grid as 2D array
    data = [list(map(int, [*i])) for i in text.splitlines()]
    length, width = (len(data), len(data[0]))

    # Initialize a grid of 1s of same size to track scenic score
    score = [[1 for i in range(width)] for i in range(length)]

    for _ in range(4):
        for i, row in enumerate(data):
            # Initialize stack with (height, index)
            stack = [(10, 0)]
            for j, height in enumerate(row):
                # If height is greater than the top of the stack, pop it
                while height > stack[-1][0]:
                    stack.pop()
                # Update the score and push the new tree onto the stack
                # score = product of viewing distance in each of the four directions
                score[i][j] *= j - stack[-1][1]
                stack.append((height, j))

        # Rotate both data and score by 90 degrees
        data, score = map(rot90, (data, score))  # type: ignore

    return max([max(row) for row in score])


_input = """
30373
25512
65332
33549
35390
""".strip()
assert main(_input) == 8
