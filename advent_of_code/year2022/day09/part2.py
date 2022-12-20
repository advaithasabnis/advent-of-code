def sign(x: float) -> int:
    return (x > 0) - (x < 0)


def main(text: str) -> int:
    # Represent positions of knots as a list of complex coordinates
    # Initial position is 0+0j for all knots
    pos = [0 + 0j for _ in range(10)]
    move = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

    # Initialize variable to hold coordinates visited all knots
    visited = [{0 + 0j} for _ in range(10)]

    # Parse the motions of the head
    motions = [(m.split()) for m in text.splitlines()]

    for direction, distance in motions:
        d = int(distance)
        for _ in range(d):
            # Move the head as per the motion
            pos[0] += move[direction]
            # For every successive knot, move it towards the preceding knot
            for i in range(1, 10):
                delta = pos[i - 1] - pos[i]
                # Knot moves if it is >=2 units away from preceding knot
                if abs(delta) >= 2:
                    pos[i] += complex(sign(delta.real), sign(delta.imag))
                    visited[i].add(pos[i])

    return len(visited[9])


_input = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".strip()
assert main(_input) == 36
