rot90 = lambda A: [*map(list, zip(*A[::-1]))]


def main(text: str) -> int:
    # Read grid as 2D array
    data = [list(map(int, [*i])) for i in text.splitlines()]
    length, width = (len(data), len(data[0]))

    # Initialize a grid of 0s of same size to track tree visibility
    vis = [[0 for i in range(width)] for i in range(length)]

    for _ in range(4):
        # To check visibility from each direction, check left to right then rotate by 90
        for i, row in enumerate(data):
            highest = -1
            for j, height in enumerate(row):
                # If tree is now highest, set visibility to 1 and update highest
                if height > highest:
                    highest = height
                    vis[i][j] = 1
        # Rotate both data and vis by 90 degrees
        data, vis = map(rot90, (data, vis))  # type: ignore

    return sum([sum(row) for row in vis])


_input = """
30373
25512
65332
33549
35390
""".strip()
assert main(_input) == 21
